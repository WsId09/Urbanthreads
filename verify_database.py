"""
DATABASE VERIFICATION SCRIPT
Run this to show your sir that database has data!
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urbanthreads.settings')
django.setup()

from shop.models import Product, Category, Order, Cart
from django.contrib.auth.models import User

print("=" * 60)
print("📊 URBANTHREADS DATABASE VERIFICATION")
print("=" * 60)
print()

# 1. Products Count
print("1️⃣ PRODUCTS IN DATABASE:")
print(f"   Total Products: {Product.objects.count()}")
print()

# 2. Show first 5 products
print("   Sample Products:")
for i, product in enumerate(Product.objects.all()[:5], 1):
    print(f"   {i}. {product.name}")
    print(f"      Price: ₹{product.price}")
    print(f"      Category: {product.category.name}")
    print(f"      Stock: {product.quantity}")
    print()

# 3. Categories
print("2️⃣ CATEGORIES IN DATABASE:")
print(f"   Total Categories: {Category.objects.count()}")
print()
print("   All Categories:")
for i, category in enumerate(Category.objects.all(), 1):
    product_count = Product.objects.filter(category=category).count()
    print(f"   {i}. {category.name} ({product_count} products)")
print()

# 4. Users
print("3️⃣ USERS IN DATABASE:")
print(f"   Total Users: {User.objects.count()}")
print()
admin_user = User.objects.filter(is_superuser=True).first()
if admin_user:
    print(f"   Admin User: {admin_user.username}")
    print(f"   Email: {admin_user.email}")
    print(f"   Superuser: Yes ✅")
print()

# 5. Orders
print("4️⃣ ORDERS IN DATABASE:")
order_count = Order.objects.count()
print(f"   Total Orders: {order_count}")
if order_count > 0:
    print()
    print("   Recent Orders:")
    for order in Order.objects.all()[:5]:
        print(f"   - Order #{order.order_number}")
        print(f"     Customer: {order.full_name}")
        print(f"     Total: ₹{order.total_amount}")
        print(f"     Status: {order.status}")
        print()
else:
    print("   (No orders yet - place an order to see)")
print()

# 6. Database Statistics
print("5️⃣ DATABASE STATISTICS:")
featured = Product.objects.filter(is_featured=True).count()
on_sale = Product.objects.filter(is_on_sale=True).count()
print(f"   Featured Products: {featured}")
print(f"   Products on Sale: {on_sale}")
print(f"   Available Stock: {sum([p.quantity for p in Product.objects.all()])} items")
print()

# 7. Price Range
print("6️⃣ PRICE RANGE:")
prices = [p.price for p in Product.objects.all()]
if prices:
    print(f"   Minimum Price: ₹{min(prices)}")
    print(f"   Maximum Price: ₹{max(prices)}")
    print(f"   Average Price: ₹{sum(prices)//len(prices)}")
print()

print("=" * 60)
print("✅ DATABASE VERIFICATION COMPLETE!")
print("=" * 60)
print()
print("📍 Database Location: db.sqlite3")
print("🔗 Admin Panel: http://localhost:8000/admin")
print("👤 Login: admin / admin123")
print()
print("All data is stored in the database and fetched dynamically! ✅")
