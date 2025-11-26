import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urbanthreads.settings')
django.setup()

from django.contrib.auth.models import User
from shop.models import Category, Product

# Create superuser
print("Creating superuser...")
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@urbanthreads.com', 'admin123')
    print("✓ Superuser created: username='admin', password='admin123'")
else:
    print("✓ Superuser already exists")

# Create categories
print("\nCreating categories...")
categories_data = [
    {
        'name': 'Men\'s Clothing',
        'description': 'Stylish and comfortable clothing for men'
    },
    {
        'name': 'Women\'s Clothing',
        'description': 'Trendy and elegant clothing for women'
    },
    {
        'name': 'Jackets & Coats',
        'description': 'Stay warm and stylish'
    },
    {
        'name': 'Activewear',
        'description': 'Performance clothing for an active lifestyle'
    },
    {
        'name': 'Accessories',
        'description': 'Complete your look with our accessories'
    },
]

for cat_data in categories_data:
    category, created = Category.objects.get_or_create(
        name=cat_data['name'],
        defaults={'description': cat_data['description']}
    )
    if created:
        print(f"✓ Created category: {category.name}")
    else:
        print(f"✓ Category exists: {category.name}")

# Create sample products
print("\nCreating sample products...")
products_data = [
    {
        'name': 'Classic Denim Jacket',
        'description': 'Timeless denim jacket with premium finish. Perfect for casual outings and layering. Made with high-quality denim fabric.',
        'price': 2999,
        'discount_price': 2499,
        'quantity': 50,
        'category': 'Jackets & Coats',
        'sizes': 'S,M,L,XL,XXL',
        'colors': 'Blue,Black',
        'is_featured': True,
    },
    {
        'name': 'Floral Summer Dress',
        'description': 'Light and breezy floral print dress. Perfect for summer days. Comfortable fit with elegant design.',
        'price': 1899,
        'quantity': 30,
        'category': 'Women\'s Clothing',
        'sizes': 'XS,S,M,L',
        'colors': 'Pink,Blue,Yellow',
        'is_featured': True,
    },
    {
        'name': 'Premium Cotton T-Shirt',
        'description': '100% organic cotton t-shirt. Ultra comfortable and breathable. Perfect for everyday wear.',
        'price': 899,
        'discount_price': 699,
        'quantity': 100,
        'category': 'Men\'s Clothing',
        'sizes': 'S,M,L,XL,XXL',
        'colors': 'White,Black,Navy,Gray',
        'is_featured': False,
    },
    {
        'name': 'Elegant Blazer',
        'description': 'Professional and stylish blazer. Perfect for office and formal occasions. Tailored fit.',
        'price': 4599,
        'quantity': 20,
        'category': 'Women\'s Clothing',
        'sizes': 'S,M,L,XL',
        'colors': 'Black,Navy,Beige',
        'is_featured': True,
    },
    {
        'name': 'Casual Chinos',
        'description': 'Perfect fit casual chinos. Comfortable for all-day wear. Multiple color options available.',
        'price': 1799,
        'quantity': 60,
        'category': 'Men\'s Clothing',
        'sizes': '30,32,34,36,38',
        'colors': 'Khaki,Navy,Black',
        'is_featured': False,
    },
    {
        'name': 'Sports Performance Leggings',
        'description': 'High-performance athletic leggings. Moisture-wicking fabric. Perfect for workouts and yoga.',
        'price': 1299,
        'discount_price': 999,
        'quantity': 40,
        'category': 'Activewear',
        'sizes': 'XS,S,M,L,XL',
        'colors': 'Black,Navy,Purple',
        'is_featured': True,
    },
    {
        'name': 'Hooded Sweatshirt',
        'description': 'Cozy and stylish hoodie. Perfect for cooler weather. Soft fleece interior.',
        'price': 1599,
        'quantity': 45,
        'category': 'Men\'s Clothing',
        'sizes': 'S,M,L,XL,XXL',
        'colors': 'Gray,Black,Navy',
        'is_featured': False,
    },
    {
        'name': 'Leather Crossbody Bag',
        'description': 'Elegant leather crossbody bag. Perfect size for essentials. Multiple compartments.',
        'price': 3499,
        'discount_price': 2999,
        'quantity': 25,
        'category': 'Accessories',
        'sizes': 'One Size',
        'colors': 'Brown,Black,Tan',
        'is_featured': True,
    },
    {
        'name': 'Running Shorts',
        'description': 'Lightweight running shorts. Quick-dry fabric. Built-in liner for comfort.',
        'price': 799,
        'quantity': 70,
        'category': 'Activewear',
        'sizes': 'S,M,L,XL',
        'colors': 'Black,Navy,Red',
        'is_featured': False,
    },
    {
        'name': 'Wool Blend Overcoat',
        'description': 'Classic wool blend overcoat. Perfect for winter. Warm and stylish.',
        'price': 5999,
        'discount_price': 4999,
        'quantity': 15,
        'category': 'Jackets & Coats',
        'sizes': 'M,L,XL,XXL',
        'colors': 'Charcoal,Camel,Navy',
        'is_featured': True,
    },
]

for prod_data in products_data:
    category = Category.objects.get(name=prod_data['category'])
    product, created = Product.objects.get_or_create(
        name=prod_data['name'],
        defaults={
            'description': prod_data['description'],
            'price': prod_data['price'],
            'discount_price': prod_data.get('discount_price'),
            'quantity': prod_data['quantity'],
            'category': category,
            'sizes': prod_data['sizes'],
            'colors': prod_data['colors'],
            'is_featured': prod_data['is_featured'],
            'photo': 'products/placeholder.jpg',  # You'll need to add actual images
        }
    )
    if created:
        print(f"✓ Created product: {product.name}")
    else:
        print(f"✓ Product exists: {product.name}")

print("\n" + "="*50)
print("Database setup complete!")
print("="*50)
print("\nAdmin credentials:")
print("Username: admin")
print("Password: admin123")
print("\nAccess admin panel at: http://localhost:8000/admin/")
print("="*50)
