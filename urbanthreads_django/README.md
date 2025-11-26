# UrbanThreads - Premium E-Commerce Platform

A complete, production-ready Django e-commerce website for clothing store with modern UI, admin panel, and full CRUD functionality.

![Django](https://img.shields.io/badge/Django-5.2.8-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.2-purple.svg)

## 🚀 Features

### User Features
- ✅ User Registration & Authentication
- ✅ Product Browsing with Categories
- ✅ Advanced Product Search & Filters
- ✅ Product Details with Multiple Variants (Size, Color)
- ✅ Shopping Cart Management
- ✅ Secure Checkout Process
- ✅ Order History & Tracking
- ✅ Responsive Design (Mobile-Friendly)

### Admin Features
- ✅ Full CRUD Operations for Categories
- ✅ Full CRUD Operations for Products
- ✅ Product Image Management
- ✅ Order Management
- ✅ User Management
- ✅ Inventory Tracking
- ✅ Sales & Discount Management

## 📋 Requirements

- Python 3.8+
- Django 5.2.8
- SQLite (default) or MySQL
- Pillow (for image handling)

## 🛠️ Installation & Setup

### 1. Clone or Extract the Project
```bash
cd urbanthreads_django
```

### 2. Install Dependencies
```bash
pip install django pillow --break-system-packages
```

### 3. Database Setup
The database is already set up with migrations. If you need to reset:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin User (Already Done)
Admin credentials are already created:
- **Username:** admin
- **Password:** admin123

If you need to create a new superuser:
```bash
python manage.py createsuperuser
```

### 5. Populate Sample Data (Already Done)
Sample data is already loaded. To reload:
```bash
python populate_db.py
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The website will be available at: `http://localhost:8000`

## 🎯 Access Points

### Public Website
- **Home:** http://localhost:8000/
- **Products:** http://localhost:8000/products/
- **Login:** http://localhost:8000/login/
- **Register:** http://localhost:8000/register/

### Admin Panel
- **Admin Dashboard:** http://localhost:8000/admin/
- **Username:** admin
- **Password:** admin123

## 📁 Project Structure

```
urbanthreads_django/
├── urbanthreads/          # Project settings
│   ├── settings.py        # Configuration
│   ├── urls.py           # Main URL routing
│   └── ...
├── shop/                  # Main shop application
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── admin.py          # Admin configuration
│   ├── urls.py           # App URL routing
│   └── ...
├── accounts/             # User authentication app
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── shop/            # Shop templates
│   └── accounts/        # Auth templates
├── static/              # Static files (CSS, JS, Images)
├── media/               # User uploaded files
├── populate_db.py       # Database population script
└── manage.py           # Django management script
```

## 🗃️ Database Models

### Category
- Name
- Description
- Image
- Slug (auto-generated)
- Active status

### Product
- Name
- Description
- Price
- Discount Price
- Quantity
- Category (Foreign Key)
- Photo
- Sizes (comma-separated)
- Colors (comma-separated)
- Featured status
- Slug (auto-generated)

### Cart
- User (Foreign Key)
- Product (Foreign Key)
- Quantity
- Size
- Color

### Order
- User (Foreign Key)
- Order Number (auto-generated)
- Status (Pending, Processing, Shipped, Delivered)
- Total Amount
- Shipping Information
- Timestamps

### OrderItem
- Order (Foreign Key)
- Product (Foreign Key)
- Quantity
- Price
- Size
- Color

## 🎨 Admin Panel Features

### Categories Management
- Add/Edit/Delete categories
- Upload category images
- Toggle active status
- Automatic slug generation

### Products Management
- Add/Edit/Delete products
- Upload product images
- Set prices and discounts
- Manage inventory (quantity)
- Add size and color variants
- Mark products as featured
- Bulk actions support

### Orders Management
- View all orders
- Update order status
- View order details
- Filter by status
- Search by order number/customer

## 📝 Sample Data

The system comes pre-loaded with:
- ✅ 5 Categories (Men's, Women's, Jackets, Activewear, Accessories)
- ✅ 10 Products with various variants
- ✅ Admin user (username: admin, password: admin123)

## 🔒 Security Features

- CSRF Protection
- Password Hashing
- Login Required for Cart/Checkout
- Admin Authentication
- Secure Form Validation

## 📱 Responsive Design

The website is fully responsive and works on:
- 💻 Desktop
- 📱 Tablets
- 📱 Mobile phones

## 🎨 Design Features

- Modern gradient UI
- Smooth animations
- Card-based layout
- Bootstrap 5 components
- Font Awesome icons
- Google Fonts (Inter)

## 🔄 Workflow

### Customer Journey
1. Browse products
2. View product details
3. Add to cart
4. Login/Register
5. Checkout
6. Place order
7. Track order

### Admin Workflow
1. Login to admin panel
2. Manage categories
3. Add/Update products
4. Process orders
5. Update inventory
6. Manage users

## 🚀 Future Enhancements

- Payment Gateway Integration
- Email Notifications
- Product Reviews & Ratings
- Wishlist Feature
- Advanced Analytics
- Multi-image Gallery
- Size Guide
- Stock Alerts

## 📧 Support

For any issues or questions, please refer to Django documentation or contact the development team.

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Developer Notes

- Models use proper relationships (ForeignKey, related_name)
- Views follow DRY principle
- Templates extend base template
- Admin panel customized for better UX
- Static files properly configured
- Media files handling implemented
- URL patterns organized
- Forms with validation
- Messages framework integrated
- Responsive design implemented

---

**Built with ❤️ using Django & Bootstrap**
