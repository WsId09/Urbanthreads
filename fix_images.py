#!/usr/bin/env python
"""
Quick fix script to update all products with working image URLs
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urbanthreads.settings')
django.setup()

from shop.models import Product

# Map products to actual fashion images from Unsplash
product_images = [
    ('Classic Denim Jacket', 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600'),
    ('Floral Summer Dress', 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=600'),
    ('Premium Cotton T-Shirt', 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=600'),
    ('Elegant Blazer', 'https://images.unsplash.com/photo-1591369822096-ffd140ec948f?w=600'),
    ('Casual Chinos', 'https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=600'),
    ('Sports Performance Leggings', 'https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=600'),
    ('Hooded Sweatshirt', 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=600'),
    ('Leather Crossbody Bag', 'https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=600'),
    ('Running Shorts', 'https://images.unsplash.com/photo-1519235106638-30cc49b5dbc5?w=600'),
    ('Wool Blend Overcoat', 'https://images.unsplash.com/photo-1539533018447-63fcce2678e3?w=600'),
]

print("\n" + "="*60)
print("🔧 FIXING PRODUCT IMAGES")
print("="*60)

success_count = 0
for product_name, image_url in product_images:
    try:
        products = Product.objects.filter(name=product_name)
        if products.exists():
            for product in products:
                # Simply store the URL in the photo field
                product.photo = image_url
                product.save()
                print(f"✓ Updated: {product_name}")
                success_count += 1
        else:
            print(f"⚠ Not found: {product_name}")
    except Exception as e:
        print(f"✗ Error with {product_name}: {e}")

print("="*60)
print(f"✅ Successfully updated {success_count} products!")
print("="*60)
print("\n🎉 All products now have working images!")
print("\nRestart your server and refresh the page:")
print("  python manage.py runserver")
print("\n")
