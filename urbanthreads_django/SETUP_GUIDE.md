# 🎯 COMPLETE SETUP & USAGE GUIDE

## Quick Start (5 Minutes)

### Step 1: Navigate to Project
```bash
cd urbanthreads_django
```

### Step 2: Run Server
```bash
python manage.py runserver
```

### Step 3: Access Website
- **Website:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin
- **Admin Login:** username: `admin`, password: `admin123`

---

## 📦 What's Included

✅ Complete Django E-commerce Platform
✅ 5 Pre-loaded Categories
✅ 10 Sample Products
✅ User Authentication System
✅ Shopping Cart
✅ Checkout Process
✅ Order Management
✅ Admin Panel with CRUD Operations
✅ Responsive Bootstrap UI

---

## 🎨 Admin Panel Guide

### Accessing Admin Panel
1. Go to: http://localhost:8000/admin/
2. Login with:
   - Username: `admin`
   - Password: `admin123`

### Managing Categories
1. Click on "Categories" in admin panel
2. Click "Add Category" to create new
3. Fill in:
   - Name (required)
   - Description
   - Upload image (optional)
   - Mark as active
4. Click "Save"

### Managing Products
1. Click on "Products" in admin panel
2. Click "Add Product" to create new
3. Fill in details:
   - **Basic Info:**
     - Name (required)
     - Description (required)
     - Category (select from dropdown)
   
   - **Pricing:**
     - Price (required)
     - Discount Price (optional for sales)
   
   - **Inventory:**
     - Quantity (stock available)
     - Sizes (e.g., S,M,L,XL)
     - Colors (e.g., Red,Blue,Green)
   
   - **Media:**
     - Upload product photo (required)
   
   - **Status:**
     - Mark as Featured (shows on homepage)
     - Mark as Active (visible to users)

4. Click "Save"

### Managing Orders
1. Click on "Orders" in admin panel
2. View all customer orders
3. Update order status:
   - Pending
   - Processing
   - Shipped
   - Delivered
   - Cancelled
4. Click on order number to view details

---

## 👥 User Features Guide

### Registration
1. Go to homepage
2. Click "Sign Up" in navigation
3. Enter username and password
4. Click "Sign Up"
5. Automatically logged in

### Shopping
1. Browse products on homepage or products page
2. Click on product to view details
3. Select size and color (if available)
4. Choose quantity
5. Click "Add to Cart"

### Checkout
1. Click cart icon in navigation
2. Review items
3. Update quantities if needed
4. Click "Proceed to Checkout"
5. Fill in shipping information:
   - Full name
   - Email
   - Phone
   - Address
   - City, State, Pincode
6. Click "Place Order"

### Order Tracking
1. Click "My Orders" in navigation
2. View all your orders
3. Click "View Details" on any order
4. See order status and items

---

## 🗂️ Database Structure

### Categories Table
- id (Primary Key)
- name
- slug (auto-generated)
- description
- image
- is_active
- created_at, updated_at

### Products Table
- id (Primary Key)
- name
- slug (auto-generated)
- description
- price
- discount_price
- quantity
- category_id (Foreign Key)
- photo
- sizes
- colors
- is_featured
- is_active
- created_at, updated_at

### Orders Table
- id (Primary Key)
- user_id (Foreign Key)
- order_number
- total_amount
- status
- full_name, email, phone
- address, city, state, pincode
- created_at, updated_at

### Order Items Table
- id (Primary Key)
- order_id (Foreign Key)
- product_id (Foreign Key)
- quantity
- price
- size, color

---

## 🔧 Customization Guide

### Changing Colors
Edit `/templates/base.html` and modify CSS variables:
```css
:root {
    --primary-color: #667eea;  /* Change this */
    --secondary-color: #764ba2; /* And this */
}
```

### Adding New Category
1. Admin Panel → Categories → Add Category
2. Or programmatically:
```python
Category.objects.create(
    name='New Category',
    description='Description here'
)
```

### Adding New Product
1. Admin Panel → Products → Add Product
2. Or programmatically:
```python
Product.objects.create(
    name='Product Name',
    description='Description',
    price=999,
    quantity=50,
    category=category_object,
    photo='path/to/image.jpg'
)
```

---

## 🐛 Troubleshooting

### Server Won't Start
```bash
# Check if port 8000 is in use
# Try different port
python manage.py runserver 8080
```

### Can't Login to Admin
```bash
# Create new superuser
python manage.py createsuperuser
```

### Database Issues
```bash
# Delete database and start fresh
rm db.sqlite3
python manage.py migrate
python populate_db.py
```

### Images Not Showing
1. Check if `media/` folder exists
2. Verify `MEDIA_URL` and `MEDIA_ROOT` in settings.py
3. Upload images through admin panel

---

## 📊 Sample Testing Flow

### Test User Registration
1. Go to http://localhost:8000
2. Click "Sign Up"
3. Enter username: `testuser`, password: `test1234`
4. Should redirect to homepage

### Test Product Browsing
1. Homepage shows featured products
2. Click "Products" to see all
3. Use filters (category, price)
4. Click on product to see details

### Test Shopping Cart
1. Add product to cart
2. View cart (icon in navbar)
3. Update quantity
4. Remove items
5. Proceed to checkout

### Test Order Placement
1. Fill shipping info
2. Place order
3. View order in "My Orders"
4. Check order status

### Test Admin Functions
1. Login to admin
2. Add new category
3. Add new product
4. View orders
5. Update order status

---

## 🚀 Production Deployment Tips

### Before Deployment:
1. Change `DEBUG = False` in settings.py
2. Set `ALLOWED_HOSTS` in settings.py
3. Use environment variables for secrets
4. Set up proper database (PostgreSQL/MySQL)
5. Configure static files collection
6. Set up media file storage
7. Enable HTTPS
8. Add email backend
9. Configure payment gateway

### Security Checklist:
- [ ] Change SECRET_KEY
- [ ] Set DEBUG = False
- [ ] Configure ALLOWED_HOSTS
- [ ] Use strong passwords
- [ ] Enable HTTPS
- [ ] Set up CSRF protection
- [ ] Configure CORS if needed
- [ ] Set up backup system

---

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [Python Package Index](https://pypi.org/)

---

## ✅ Checklist for Your Submission

- [x] Database with MySQL-compatible structure (using SQLite for development)
- [x] Minimum 5 categories
- [x] Product model with all required fields
- [x] User authentication (Django's built-in)
- [x] Bootstrap template for frontend
- [x] Login and Sign Up pages
- [x] Dynamic homepage
- [x] Product listing/category pages
- [x] 10 individual product pages
- [x] Admin panel (Django Admin)
- [x] AdminLTE-style interface
- [x] Admin login separate from user login
- [x] Full CRUD for categories
- [x] Full CRUD for products
- [x] Dynamic content management

---

**Your complete Django e-commerce platform is ready! 🎉**

For any questions or issues, refer to the README.md or Django documentation.
