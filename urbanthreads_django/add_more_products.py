#!/usr/bin/env python
"""
Add more products to each category (at least 5-8 products per category)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urbanthreads.settings')
django.setup()

from shop.models import Category, Product

# Additional products with variety
new_products = [
    # Men's Clothing (more items)
    {
        'name': 'Slim Fit Formal Shirt',
        'description': 'Professional slim fit formal shirt. Perfect for office wear. Premium cotton blend with wrinkle-resistant fabric.',
        'price': 1299,
        'discount_price': 999,
        'quantity': 80,
        'category': 'Men\'s Clothing',
        'sizes': 'S M L XL XXL',
        'colors': 'White Black Blue Pink',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1620012253295-c15cc3e65df4?w=600',
    },
    {
        'name': 'Cargo Pants',
        'description': 'Utility cargo pants with multiple pockets. Comfortable and durable for outdoor activities.',
        'price': 2299,
        'quantity': 45,
        'category': 'Men\'s Clothing',
        'sizes': '30 32 34 36 38 40',
        'colors': 'Olive Green Khaki Black',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=600',
    },
    {
        'name': 'V-Neck Sweater',
        'description': 'Classic v-neck sweater in pure wool. Perfect for layering in winter season.',
        'price': 1899,
        'discount_price': 1499,
        'quantity': 35,
        'category': 'Men\'s Clothing',
        'sizes': 'M L XL XXL',
        'colors': 'Navy Burgundy Gray Black',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=600',
    },
    {
        'name': 'Polo T-Shirt',
        'description': 'Classic polo t-shirt with collar. Made from breathable pique cotton fabric.',
        'price': 1099,
        'quantity': 90,
        'category': 'Men\'s Clothing',
        'sizes': 'S M L XL XXL',
        'colors': 'White Black Navy Red Yellow',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=600',
    },
    {
        'name': 'Track Pants',
        'description': 'Comfortable track pants for sports and casual wear. Elastic waistband with drawstring.',
        'price': 899,
        'quantity': 70,
        'category': 'Men\'s Clothing',
        'sizes': 'S M L XL XXL',
        'colors': 'Black Navy Gray',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1552902865-b72c031ac5ea?w=600',
    },
    
    # Women's Clothing (more items)
    {
        'name': 'A-Line Midi Skirt',
        'description': 'Elegant A-line midi skirt. Perfect for office and casual occasions. Comfortable fit with side zipper.',
        'price': 1599,
        'discount_price': 1199,
        'quantity': 50,
        'category': 'Women\'s Clothing',
        'sizes': 'XS S M L XL',
        'colors': 'Black Navy Red Beige',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=600',
    },
    {
        'name': 'Casual Jumpsuit',
        'description': 'Comfortable casual jumpsuit with adjustable straps. Perfect for summer outings.',
        'price': 2299,
        'quantity': 30,
        'category': 'Women\'s Clothing',
        'sizes': 'S M L XL',
        'colors': 'Black Blue Olive Green',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=600',
    },
    {
        'name': 'Printed Kurti',
        'description': 'Beautiful printed kurti with intricate designs. Comfortable cotton fabric perfect for daily wear.',
        'price': 999,
        'discount_price': 799,
        'quantity': 60,
        'category': 'Women\'s Clothing',
        'sizes': 'S M L XL XXL',
        'colors': 'Red Blue Green Yellow Pink',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=600',
    },
    {
        'name': 'Formal Trousers',
        'description': 'Professional formal trousers for women. Slim fit with perfect drape and comfortable wear.',
        'price': 1799,
        'quantity': 45,
        'category': 'Women\'s Clothing',
        'sizes': '28 30 32 34 36',
        'colors': 'Black Gray Navy Beige',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=600',
    },
    {
        'name': 'Maxi Dress',
        'description': 'Flowing maxi dress perfect for parties and special occasions. Comfortable and stylish.',
        'price': 2499,
        'discount_price': 1999,
        'quantity': 25,
        'category': 'Women\'s Clothing',
        'sizes': 'XS S M L XL',
        'colors': 'Black Red Navy Burgundy',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=600',
    },
    
    # Jackets & Coats (more items)
    {
        'name': 'Bomber Jacket',
        'description': 'Trendy bomber jacket with ribbed cuffs and hem. Perfect for casual styling.',
        'price': 3499,
        'discount_price': 2999,
        'quantity': 30,
        'category': 'Jackets & Coats',
        'sizes': 'M L XL XXL',
        'colors': 'Black Olive Green Navy',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600',
    },
    {
        'name': 'Leather Jacket',
        'description': 'Genuine leather jacket with asymmetric zipper. Premium quality and timeless style.',
        'price': 8999,
        'discount_price': 7499,
        'quantity': 15,
        'category': 'Jackets & Coats',
        'sizes': 'S M L XL',
        'colors': 'Black Brown',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600',
    },
    {
        'name': 'Puffer Jacket',
        'description': 'Warm puffer jacket with hood. Water-resistant and perfect for cold weather.',
        'price': 4599,
        'quantity': 40,
        'category': 'Jackets & Coats',
        'sizes': 'M L XL XXL',
        'colors': 'Black Navy Red',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1544022613-e87ca75a784a?w=600',
    },
    {
        'name': 'Windbreaker',
        'description': 'Lightweight windbreaker jacket. Perfect for outdoor activities and sports.',
        'price': 1999,
        'discount_price': 1599,
        'quantity': 55,
        'category': 'Jackets & Coats',
        'sizes': 'S M L XL XXL',
        'colors': 'Blue Black Red Yellow',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=600',
    },
    
    # Activewear (more items)
    {
        'name': 'Compression Tights',
        'description': 'High-performance compression tights for running and gym. Moisture-wicking fabric.',
        'price': 1599,
        'quantity': 60,
        'category': 'Activewear',
        'sizes': 'S M L XL',
        'colors': 'Black Navy Purple',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=600',
    },
    {
        'name': 'Sports Bra',
        'description': 'High-support sports bra for intense workouts. Breathable and comfortable.',
        'price': 999,
        'discount_price': 799,
        'quantity': 80,
        'category': 'Activewear',
        'sizes': 'XS S M L XL',
        'colors': 'Black White Pink Navy',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1518398046578-8cca57782e17?w=600',
    },
    {
        'name': 'Training Shorts',
        'description': 'Comfortable training shorts with moisture-wicking technology. Perfect for gym and sports.',
        'price': 799,
        'quantity': 85,
        'category': 'Activewear',
        'sizes': 'S M L XL XXL',
        'colors': 'Black Navy Gray Red',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1519235106638-30cc49b5dbc5?w=600',
    },
    {
        'name': 'Yoga Pants',
        'description': 'Flexible yoga pants with high waist. Perfect for yoga and pilates.',
        'price': 1299,
        'quantity': 70,
        'category': 'Activewear',
        'sizes': 'XS S M L XL',
        'colors': 'Black Purple Blue Gray',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=600',
    },
    {
        'name': 'Athletic T-Shirt',
        'description': 'Breathable athletic t-shirt for sports. Quick-dry fabric with anti-odor technology.',
        'price': 699,
        'discount_price': 499,
        'quantity': 100,
        'category': 'Activewear',
        'sizes': 'S M L XL XXL',
        'colors': 'Black White Gray Blue Red',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=600',
    },
    
    # Accessories (more items)
    {
        'name': 'Canvas Backpack',
        'description': 'Durable canvas backpack with laptop compartment. Perfect for daily use and travel.',
        'price': 1999,
        'discount_price': 1599,
        'quantity': 50,
        'category': 'Accessories',
        'sizes': 'One Size',
        'colors': 'Black Gray Navy Olive',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=600',
    },
    {
        'name': 'Leather Belt',
        'description': 'Classic leather belt with metal buckle. Essential accessory for formal and casual wear.',
        'price': 799,
        'quantity': 90,
        'category': 'Accessories',
        'sizes': '32 34 36 38 40 42',
        'colors': 'Black Brown Tan',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1624222247344-550fb60583bb?w=600',
    },
    {
        'name': 'Wool Scarf',
        'description': 'Soft wool scarf to keep you warm. Perfect winter accessory with elegant design.',
        'price': 699,
        'discount_price': 499,
        'quantity': 60,
        'category': 'Accessories',
        'sizes': 'One Size',
        'colors': 'Black Gray Navy Burgundy Beige',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1520903920243-00d872a2d1c9?w=600',
    },
    {
        'name': 'Baseball Cap',
        'description': 'Classic baseball cap with adjustable strap. Perfect for casual outings.',
        'price': 599,
        'quantity': 100,
        'category': 'Accessories',
        'sizes': 'One Size',
        'colors': 'Black White Navy Red',
        'is_featured': True,
        'image_url': 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=600',
    },
    {
        'name': 'Tote Bag',
        'description': 'Spacious tote bag for shopping and daily use. Eco-friendly canvas material.',
        'price': 899,
        'quantity': 70,
        'category': 'Accessories',
        'sizes': 'One Size',
        'colors': 'Black Beige Navy',
        'is_featured': False,
        'image_url': 'https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=600',
    },
]

print("\n" + "="*70)
print("📦 ADDING MORE PRODUCTS TO ALL CATEGORIES")
print("="*70 + "\n")

success_count = 0
for prod_data in new_products:
    try:
        category = Category.objects.get(name=prod_data['category'])
        
        # Check if product already exists
        if not Product.objects.filter(name=prod_data['name']).exists():
            product = Product.objects.create(
                name=prod_data['name'],
                description=prod_data['description'],
                price=prod_data['price'],
                discount_price=prod_data.get('discount_price'),
                quantity=prod_data['quantity'],
                category=category,
                sizes=prod_data['sizes'],
                colors=prod_data['colors'],
                is_featured=prod_data['is_featured'],
                image_url=prod_data['image_url'],
            )
            print(f"✓ Added: {product.name} ({category.name})")
            success_count += 1
        else:
            print(f"⚠ Already exists: {prod_data['name']}")
            
    except Category.DoesNotExist:
        print(f"✗ Category not found: {prod_data['category']}")
    except Exception as e:
        print(f"✗ Error: {prod_data['name']} - {e}")

print("\n" + "="*70)
print(f"✅ Successfully added {success_count} new products!")
print("="*70)

# Show summary by category
print("\n📊 PRODUCT COUNT BY CATEGORY:")
print("-" * 70)
for cat in Category.objects.all():
    count = Product.objects.filter(category=cat).count()
    print(f"  {cat.name}: {count} products")
print("-" * 70)
print("\n🎉 All categories now have plenty of products!\n")
