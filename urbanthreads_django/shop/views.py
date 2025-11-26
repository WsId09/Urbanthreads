from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product, Cart, Order, OrderItem
import uuid

def home(request):
    """Home page with featured products and categories"""
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:8]
    categories = Category.objects.filter(is_active=True)[:6]
    new_arrivals = Product.objects.filter(is_active=True).order_by('-created_at')[:4]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'new_arrivals': new_arrivals,
    }
    return render(request, 'shop/home.html', context)

def product_list(request):
    """List all products with filtering options"""
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Price filter
    price_filter = request.GET.get('price')
    if price_filter == 'low':
        products = products.filter(price__lt=2000)
    elif price_filter == 'mid':
        products = products.filter(price__gte=2000, price__lte=4000)
    elif price_filter == 'high':
        products = products.filter(price__gt=4000)
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/product_list.html', context)

def product_detail(request, slug):
    """Individual product detail page"""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category, 
        is_active=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'shop/product_detail.html', context)

def category_products(request, slug):
    """Products by category"""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = Product.objects.filter(category=category, is_active=True)
    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'shop/category_products.html', context)

@login_required
def add_to_cart(request, product_id):
    """Add product to cart"""
    product = get_object_or_404(Product, id=product_id)
    
    size = request.POST.get('size', '')
    color = request.POST.get('color', '')
    quantity = int(request.POST.get('quantity', 1))
    
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        size=size,
        color=color,
        defaults={'quantity': quantity}
    )
    
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    messages.success(request, f'{product.name} added to cart!')
    return redirect('cart')

@login_required
def cart(request):
    """View cart"""
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'shop/cart.html', context)

@login_required
def update_cart(request, cart_id):
    """Update cart item quantity"""
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, 'Cart updated!')
    else:
        cart_item.delete()
        messages.success(request, 'Item removed from cart!')
    
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('cart')

@login_required
def checkout(request):
    """Checkout page"""
    cart_items = Cart.objects.filter(user=request.user)
    
    if not cart_items:
        messages.warning(request, 'Your cart is empty!')
        return redirect('product_list')
    
    total = sum(item.total_price for item in cart_items)
    
    if request.method == 'POST':
        # Create order
        order = Order.objects.create(
            user=request.user,
            order_number=f'ORD-{uuid.uuid4().hex[:10].upper()}',
            total_amount=total,
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            pincode=request.POST.get('pincode'),
        )
        
        # Create order items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.final_price,
                size=item.size,
                color=item.color,
            )
            
            # Update product quantity
            item.product.quantity -= item.quantity
            item.product.save()
        
        # Clear cart
        cart_items.delete()
        
        messages.success(request, f'Order placed successfully! Order number: {order.order_number}')
        return redirect('order_detail', order_id=order.id)
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'shop/checkout.html', context)

@login_required
def orders(request):
    """User's order history"""
    user_orders = Order.objects.filter(user=request.user)
    
    context = {
        'orders': user_orders,
    }
    return render(request, 'shop/orders.html', context)

@login_required
def order_detail(request, order_id):
    """Individual order detail"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
    }
    return render(request, 'shop/order_detail.html', context)

# Authentication views
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from accounts.forms import CustomUserCreationForm

def user_register(request):
    """User registration with email"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to UrbanThreads!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def user_login(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def user_logout(request):
    """User logout"""
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

@login_required
def download_invoice(request, order_id):
    """Generate and download invoice PDF"""
    from django.http import HttpResponse
    from datetime import datetime
    
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Create HTML for invoice
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Invoice #{order.order_number}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                color: #333;
            }}
            .header {{
                text-align: center;
                margin-bottom: 30px;
                border-bottom: 3px solid #667eea;
                padding-bottom: 20px;
            }}
            .company-name {{
                font-size: 32px;
                font-weight: bold;
                color: #667eea;
                margin-bottom: 5px;
            }}
            .invoice-title {{
                font-size: 24px;
                margin-top: 20px;
                color: #666;
            }}
            .info-section {{
                display: flex;
                justify-content: space-between;
                margin: 30px 0;
            }}
            .info-box {{
                width: 48%;
            }}
            .info-box h3 {{
                color: #667eea;
                border-bottom: 2px solid #667eea;
                padding-bottom: 5px;
                margin-bottom: 10px;
            }}
            .info-box p {{
                margin: 5px 0;
                line-height: 1.6;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            th {{
                background-color: #667eea;
                color: white;
                padding: 12px;
                text-align: left;
            }}
            td {{
                padding: 10px;
                border-bottom: 1px solid #ddd;
            }}
            .total-section {{
                text-align: right;
                margin-top: 20px;
            }}
            .total-row {{
                margin: 5px 0;
                font-size: 16px;
            }}
            .grand-total {{
                font-size: 20px;
                font-weight: bold;
                color: #667eea;
                margin-top: 10px;
                padding-top: 10px;
                border-top: 2px solid #667eea;
            }}
            .footer {{
                margin-top: 50px;
                text-align: center;
                color: #999;
                font-size: 12px;
                border-top: 1px solid #ddd;
                padding-top: 20px;
            }}
            .status-badge {{
                display: inline-block;
                padding: 5px 15px;
                border-radius: 20px;
                font-weight: bold;
                color: white;
                background-color: #667eea;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="company-name">UrbanThreads</div>
            <div style="color: #666;">Premium Fashion Store</div>
            <div class="invoice-title">INVOICE</div>
            <div style="margin-top: 10px;">
                <span class="status-badge">{order.get_status_display()}</span>
            </div>
        </div>
        
        <div class="info-section">
            <div class="info-box">
                <h3>Invoice Details</h3>
                <p><strong>Invoice Number:</strong> {order.order_number}</p>
                <p><strong>Date:</strong> {order.created_at.strftime('%B %d, %Y')}</p>
                <p><strong>Order Status:</strong> {order.get_status_display()}</p>
            </div>
            
            <div class="info-box">
                <h3>Shipping Address</h3>
                <p><strong>{order.full_name}</strong></p>
                <p>{order.address}</p>
                <p>{order.city}, {order.state}</p>
                <p>Pincode: {order.pincode}</p>
                <p>Phone: {order.phone}</p>
                <p>Email: {order.email}</p>
            </div>
        </div>
        
        <h3 style="color: #667eea; margin-top: 30px;">Order Items</h3>
        <table>
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th>Total</th>
                </tr>
            </thead>
            <tbody>
    """
    
    # Add order items
    for item in order.items.all():
        html_content += f"""
                <tr>
                    <td>
                        <strong>{item.product.name}</strong>
                        {f'<br><small>Size: {item.size}</small>' if item.size else ''}
                        {f'<br><small>Color: {item.color}</small>' if item.color else ''}
                    </td>
                    <td>{item.quantity}</td>
                    <td>₹{item.price}</td>
                    <td>₹{item.total_price}</td>
                </tr>
        """
    
    # Calculate totals
    subtotal = order.total_amount
    shipping = 0 if subtotal > 2000 else 100
    
    html_content += f"""
            </tbody>
        </table>
        
        <div class="total-section">
            <div class="total-row">
                <strong>Subtotal:</strong> ₹{subtotal}
            </div>
            <div class="total-row">
                <strong>Shipping:</strong> {'FREE' if shipping == 0 else f'₹{shipping}'}
            </div>
            <div class="grand-total">
                <strong>Grand Total:</strong> ₹{order.total_amount}
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Thank you for shopping with UrbanThreads!</strong></p>
            <p>For any queries, contact us at: info@urbanthreads.com | +91 98765 43210</p>
            <p>Visit us at: www.urbanthreads.com</p>
            <p style="margin-top: 20px;">This is a computer-generated invoice and does not require a signature.</p>
        </div>
    </body>
    </html>
    """
    
    # Create response
    response = HttpResponse(html_content, content_type='text/html')
    response['Content-Disposition'] = f'attachment; filename="Invoice_{order.order_number}.html"'
    
    return response
