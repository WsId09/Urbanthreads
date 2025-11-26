"""
COMPLETE AUTO SETUP SCRIPT FOR URBANTHREADS
Run this ONE script to add everything!
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urbanthreads.settings')
django.setup()

from django.contrib.auth.models import User
from shop.models import Category, Product

print("=" * 60)
print("🚀 URBANTHREADS AUTO SETUP SCRIPT")
print("=" * 60)
print()

# Step 1: Create Superuser
print("1️⃣ Creating Admin User...")
try:
    if User.objects.filter(username='admin').exists():
        print("   ✅ Admin user already exists!")
    else:
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        print("   ✅ Admin user created!")
        print("   Username: admin")
        print("   Password: admin123")
except Exception as e:
    print(f"   ⚠️ Admin creation error: {e}")
print()

# Step 2: Create Categories
print("2️⃣ Creating Categories...")
categories_data = [
    {
        'name': "Men's Clothing",
        'description': "Premium menswear collection featuring suits, shirts, and accessories for the modern gentleman."
    },
    {
        'name': "Women's Clothing",
        'description': "Elegant women's fashion including dresses, tops, and contemporary styles."
    },
    {
        'name': "Jackets & Coats",
        'description': "Stay warm and stylish with our curated selection of jackets and coats."
    },
    {
        'name': "Activewear",
        'description': "High-performance sportswear designed for fitness enthusiasts."
    },
    {
        'name': "Accessories",
        'description': "Complete your look with our range of premium accessories."
    }
]

categories = {}
for cat_data in categories_data:
    cat, created = Category.objects.get_or_create(
        name=cat_data['name'],
        defaults={'description': cat_data['description']}
    )
    categories[cat_data['name']] = cat
    if created:
        print(f"   ✅ Created: {cat_data['name']}")
    else:
        print(f"   ℹ️ Exists: {cat_data['name']}")
print()

# Step 3: Create Products
print("3️⃣ Creating Products...")

products_data = [
    # Men's Clothing (8 products)
    {
        'name': 'Slim Fit Formal Shirt',
        'category': "Men's Clothing",
        'price': 1299,
        'discount_price': 999,
        'description': 'Premium cotton formal shirt with slim fit design. Perfect for office and formal events.',
        'image_url': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500',
        'quantity': 100,
        'sizes': 'S, M, L, XL, XXL',
        'colors': 'White, Blue, Black',
        'is_featured': True,
        'is_on_sale': True
    },
    {
        'name': 'Classic Business Suit',
        'category': "Men's Clothing",
        'price': 8999,
        'discount_price': 7499,
        'description': 'Two-piece business suit in premium wool blend fabric.',
        'image_url': 'https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=500',
        'quantity': 50,
        'sizes': 'M, L, XL',
        'colors': 'Navy, Charcoal, Black',
        'is_featured': True,
        'is_on_sale': True
    },
    {
        'name': 'Casual Polo Shirt',
        'category': "Men's Clothing",
        'price': 999,
        'discount_price': 799,
        'description': 'Comfortable cotton polo shirt for casual wear.',
        'image_url': 'https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=500',
        'quantity': 150,
        'sizes': 'S, M, L, XL',
        'colors': 'Red, Blue, Green, White',
        'is_on_sale': True
    },
    {
        'name': 'Denim Jeans',
        'category': "Men's Clothing",
        'price': 2499,
        'discount_price': 1999,
        'description': 'Classic fit denim jeans in premium quality fabric.',
        'image_url': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=500',
        'quantity': 120,
        'sizes': '30, 32, 34, 36, 38',
        'colors': 'Blue, Black, Grey',
        'is_on_sale': True
    },
    {
        'name': 'Leather Belt',
        'category': "Men's Clothing",
        'price': 899,
        'discount_price': 699,
        'description': 'Genuine leather belt with metal buckle.',
        'image_url': 'https://images.unsplash.com/photo-1624222247344-550fb60583c2?w=500',
        'quantity': 80,
        'sizes': 'Free Size',
        'colors': 'Brown, Black',
        'is_on_sale': True
    },
    {
        'name': 'Cotton Chinos',
        'category': "Men's Clothing",
        'price': 1799,
        'discount_price': 1399,
        'description': 'Comfortable chinos perfect for casual and semi-formal occasions.',
        'image_url': 'https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=500',
        'quantity': 90,
        'sizes': '30, 32, 34, 36',
        'colors': 'Khaki, Navy, Olive',
        'is_on_sale': True
    },
    {
        'name': 'V-Neck T-Shirt',
        'category': "Men's Clothing",
        'price': 599,
        'discount_price': 449,
        'description': 'Basic v-neck t-shirt in soft cotton fabric.',
        'image_url': 'https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500',
        'quantity': 200,
        'sizes': 'S, M, L, XL, XXL',
        'colors': 'Black, White, Grey, Navy',
        'is_on_sale': True
    },
    {
        'name': 'Formal Trousers',
        'category': "Men's Clothing",
        'price': 1999,
        'discount_price': 1599,
        'description': 'Classic formal trousers with perfect fit.',
        'image_url': 'https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=500',
        'quantity': 70,
        'sizes': '30, 32, 34, 36, 38',
        'colors': 'Black, Navy, Grey',
        'is_on_sale': True
    },
    
    # Women's Clothing (7 products)
    {
        'name': 'Floral Summer Dress',
        'category': "Women's Clothing",
        'price': 2499,
        'discount_price': 1999,
        'description': 'Beautiful floral print summer dress perfect for any occasion.',
        'image_url': 'https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=500',
        'quantity': 60,
        'sizes': 'XS, S, M, L, XL',
        'colors': 'Floral Print',
        'is_featured': True,
        'is_on_sale': True
    },
    {
        'name': 'Silk Blouse',
        'category': "Women's Clothing",
        'price': 1799,
        'discount_price': 1399,
        'description': 'Elegant silk blouse for formal and casual wear.',
        'image_url': 'https://images.unsplash.com/photo-1564257577-9a0b7f4e5f4c?w=500',
        'quantity': 80,
        'sizes': 'S, M, L, XL',
        'colors': 'White, Cream, Pink, Blue',
        'is_on_sale': True
    },
    {
        'name': 'High-Waist Jeans',
        'category': "Women's Clothing",
        'price': 2299,
        'discount_price': 1799,
        'description': 'Trendy high-waist jeans with perfect fit.',
        'image_url': 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=500',
        'quantity': 100,
        'sizes': '26, 28, 30, 32, 34',
        'colors': 'Blue, Black',
        'is_featured': True,
        'is_on_sale': True
    },
    {
        'name': 'Maxi Skirt',
        'category': "Women's Clothing",
        'price': 1599,
        'discount_price': 1199,
        'description': 'Flowing maxi skirt in premium fabric.',
        'image_url': 'https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=500',
        'quantity': 70,
        'sizes': 'S, M, L, XL',
        'colors': 'Black, Navy, Burgundy',
        'is_on_sale': True
    },
    {
        'name': 'Wrap Top',
        'category': "Women's Clothing",
        'price': 1299,
        'discount_price': 999,
        'description': 'Stylish wrap top perfect for any season.',
        'image_url': 'https://images.unsplash.com/photo-1624206112918-b663801ff5d3?w=500',
        'quantity': 90,
        'sizes': 'XS, S, M, L',
        'colors': 'Red, Blue, Green, Black',
        'is_on_sale': True
    },
    {
        'name': 'Evening Gown',
        'category': "Women's Clothing",
        'price': 5999,
        'discount_price': 4999,
        'description': 'Stunning evening gown for special occasions.',
        'image_url': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=500',
        'quantity': 30,
        'sizes': 'S, M, L',
        'colors': 'Black, Red, Navy',
        'is_featured': True,
        'is_on_sale': True
    },
    {
        'name': 'Casual T-Shirt Dress',
        'category': "Women's Clothing",
        'price': 999,
        'discount_price': 799,
        'description': 'Comfortable t-shirt dress for everyday wear.',
        'image_url': 'https://images.unsplash.com/photo-1612423284934-2850a4ea6b0f?w=500',
        'quantity': 120,
        'sizes': 'XS, S, M, L, XL',
        'colors': 'White, Black, Grey, Pink',
        'is_on_sale': True
    },
    
    # Jackets & Coats (6 products)
    {
        'name': 'Casual Denim Jacket',
        'category': 'Jackets & Coats',
        'price': 2999,
        'discount_price': 2499,
        'description': 'Classic denim jacket perfect for layering.',
        'image_url': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=500',
        'quantity': 80,
        'sizes': 'S, M, L, XL',
        'colors': 'Blue, Black',
        'is_featured': True,
        'is_on_sale': True
    },
    {
        'name': 'Leather Biker Jacket',
        'category': 'Jackets & Coats',
        'price': 7999,
        'discount_price': 6999,
        'description': 'Premium leather biker jacket with attitude.',
        'image_url': 'https://images.unsplash.com/photo-1520975867597-0af37a22e31e?w=500',
        'quantity': 40,
        'sizes': 'M, L, XL',
        'colors': 'Black, Brown',
        'is_featured': True,
        'is_on_sale': True
    },
    {
        'name': 'Wool Blend Overcoat',
        'category': 'Jackets & Coats',
        'price': 5999,
        'discount_price': 4999,
        'description': 'Elegant wool blend overcoat for winter.',
        'image_url': 'https://images.unsplash.com/photo-1539533113351-892c95f0c556?w=500',
        'quantity': 50,
        'sizes': 'M, L, XL, XXL',
        'colors': 'Charcoal, Navy, Camel',
        'is_on_sale': True
    },
    {
        'name': 'Puffer Jacket',
        'category': 'Jackets & Coats',
        'price': 3999,
        'discount_price': 3499,
        'description': 'Warm puffer jacket for cold weather.',
        'image_url': 'https://images.unsplash.com/photo-1544923408-75c5cef46f14?w=500',
        'quantity': 70,
        'sizes': 'S, M, L, XL',
        'colors': 'Black, Navy, Red',
        'is_on_sale': True
    },
    {
        'name': 'Bomber Jacket',
        'category': 'Jackets & Coats',
        'price': 2799,
        'discount_price': 2299,
        'description': 'Classic bomber jacket with modern fit.',
        'image_url': 'https://images.unsplash.com/photo-1521223890158-f9f7c3d5d504?w=500',
        'quantity': 60,
        'sizes': 'S, M, L, XL',
        'colors': 'Olive, Black, Navy',
        'is_on_sale': True
    },
    {
        'name': 'Trench Coat',
        'category': 'Jackets & Coats',
        'price': 4999,
        'discount_price': 3999,
        'description': 'Timeless trench coat for any season.',
        'image_url': 'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=500',
        'quantity': 45,
        'sizes': 'S, M, L, XL',
        'colors': 'Beige, Black, Navy',
        'is_on_sale': True
    },
    
    # Activewear (7 products)
    {
        'name': 'Running Shoes',
        'category': 'Activewear',
        'price': 3499,
        'discount_price': 2999,
        'description': 'High-performance running shoes with cushioned sole.',
        'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500',
        'quantity': 100,
        'sizes': '7, 8, 9, 10, 11',
        'colors': 'Black, White, Blue',
        'is_featured': True,
        'is_on_sale': True
    },
    {
        'name': 'Sports T-Shirt',
        'category': 'Activewear',
        'price': 799,
        'discount_price': 599,
        'description': 'Breathable sports t-shirt for workouts.',
        'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500',
        'quantity': 150,
        'sizes': 'S, M, L, XL, XXL',
        'colors': 'Black, Grey, Blue, Red',
        'is_on_sale': True
    },
    {
        'name': 'Yoga Pants',
        'category': 'Activewear',
        'price': 1499,
        'discount_price': 1199,
        'description': 'Flexible yoga pants with moisture-wicking fabric.',
        'image_url': 'https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=500',
        'quantity': 120,
        'sizes': 'XS, S, M, L, XL',
        'colors': 'Black, Navy, Purple',
        'is_featured': True,
        'is_on_sale': True
    },
    {
        'name': 'Sports Bra',
        'category': 'Activewear',
        'price': 999,
        'discount_price': 799,
        'description': 'Supportive sports bra for all activities.',
        'image_url': 'https://images.unsplash.com/photo-1556818255-3c2f03cf0451?w=500',
        'quantity': 100,
        'sizes': 'S, M, L, XL',
        'colors': 'Black, White, Pink',
        'is_on_sale': True
    },
    {
        'name': 'Gym Shorts',
        'category': 'Activewear',
        'price': 899,
        'discount_price': 699,
        'description': 'Comfortable gym shorts with pockets.',
        'image_url': 'https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=500',
        'quantity': 130,
        'sizes': 'S, M, L, XL',
        'colors': 'Black, Grey, Navy',
        'is_on_sale': True
    },
    {
        'name': 'Training Jacket',
        'category': 'Activewear',
        'price': 2499,
        'discount_price': 1999,
        'description': 'Lightweight training jacket with zip pockets.',
        'image_url': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500',
        'quantity': 80,
        'sizes': 'S, M, L, XL',
        'colors': 'Black, Navy, Grey',
        'is_on_sale': True
    },
    {
        'name': 'Compression Tights',
        'category': 'Activewear',
        'price': 1799,
        'discount_price': 1399,
        'description': 'Performance compression tights for athletes.',
        'image_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=500',
        'quantity': 90,
        'sizes': 'S, M, L, XL',
        'colors': 'Black, Navy',
        'is_on_sale': True
    },
    
    # Accessories (6 products)
    {
        'name': 'Baseball Cap',
        'category': 'Accessories',
        'price': 599,
        'description': 'Classic baseball cap with adjustable strap.',
        'image_url': 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=500',
        'quantity': 150,
        'sizes': 'Free Size',
        'colors': 'Black, Navy, White, Red',
        'is_featured': True
    },
    {
        'name': 'Leather Wallet',
        'category': 'Accessories',
        'price': 1299,
        'discount_price': 999,
        'description': 'Genuine leather wallet with multiple card slots.',
        'image_url': 'https://images.unsplash.com/photo-1627123424574-724758594e93?w=500',
        'quantity': 100,
        'sizes': 'Free Size',
        'colors': 'Brown, Black',
        'is_on_sale': True
    },
    {
        'name': 'Sunglasses',
        'category': 'Accessories',
        'price': 1999,
        'discount_price': 1599,
        'description': 'UV protection sunglasses with polarized lenses.',
        'image_url': 'https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=500',
        'quantity': 80,
        'sizes': 'Free Size',
        'colors': 'Black, Brown, Blue',
        'is_featured': True,
        'is_on_sale': True
    },
    {
        'name': 'Wrist Watch',
        'category': 'Accessories',
        'price': 3999,
        'discount_price': 3499,
        'description': 'Elegant wrist watch with leather strap.',
        'image_url': 'https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=500',
        'quantity': 60,
        'sizes': 'Free Size',
        'colors': 'Silver, Gold, Rose Gold',
        'is_on_sale': True
    },
    {
        'name': 'Backpack',
        'category': 'Accessories',
        'price': 2499,
        'discount_price': 1999,
        'description': 'Durable backpack with laptop compartment.',
        'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500',
        'quantity': 70,
        'sizes': 'Free Size',
        'colors': 'Black, Grey, Navy',
        'is_on_sale': True
    },
    {
        'name': 'Scarf',
        'category': 'Accessories',
        'price': 899,
        'discount_price': 699,
        'description': 'Soft wool scarf for winter.',
        'image_url': 'https://images.unsplash.com/photo-1520903920243-00d872a2d1c9?w=500',
        'quantity': 100,
        'sizes': 'Free Size',
        'colors': 'Black, Grey, Burgundy, Navy',
        'is_on_sale': True
    },
]

created_count = 0
existing_count = 0

for prod_data in products_data:
    category = categories[prod_data['category']]
    
    product, created = Product.objects.get_or_create(
        name=prod_data['name'],
        defaults={
            'category': category,
            'price': prod_data['price'],
            'discount_price': prod_data.get('discount_price', prod_data['price']),
            'description': prod_data['description'],
            'image_url': prod_data['image_url'],
            'quantity': prod_data['quantity'],
            'sizes': prod_data['sizes'],
            'colors': prod_data['colors'],
            'is_featured': prod_data.get('is_featured', False),
            'is_on_sale': prod_data.get('is_on_sale', False)
        }
    )
    
    if created:
        created_count += 1
        print(f"   ✅ Created: {prod_data['name']}")
    else:
        existing_count += 1
        print(f"   ℹ️ Exists: {prod_data['name']}")

print()
print(f"   📦 New products added: {created_count}")
print(f"   📦 Existing products: {existing_count}")
print()

# Final Summary
print("=" * 60)
print("🎉 SETUP COMPLETE!")
print("=" * 60)
print()
print("✅ Admin User: admin / admin123")
print(f"✅ Categories: {Category.objects.count()}")
print(f"✅ Products: {Product.objects.count()}")
print()
print("🌐 Visit your website: https://urbanthreads.onrender.com")
print("🔐 Admin Panel: https://urbanthreads.onrender.com/admin")
print()
print("=" * 60)
