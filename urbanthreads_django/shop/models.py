from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    photo = models.ImageField(upload_to='products/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, help_text="External image URL (optional)")
    
    # Additional fields for better e-commerce functionality
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sizes = models.CharField(max_length=100, blank=True, help_text="Comma separated sizes (e.g., S,M,L,XL)")
    colors = models.CharField(max_length=100, blank=True, help_text="Comma separated colors")
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def is_on_sale(self):
        return self.discount_price is not None and self.discount_price < self.price

    @property
    def final_price(self):
        return self.discount_price if self.is_on_sale else self.price

    @property
    def in_stock(self):
        return self.quantity > 0
    
    def get_photo_url(self):
        """Return photo URL with fallback to placeholder"""
        # First try image_url field (for external URLs)
        if self.image_url:
            return self.image_url
        # Then try uploaded photo
        try:
            if self.photo and hasattr(self.photo, 'url'):
                return self.photo.url
        except:
            pass
        # Fallback placeholder image
        return 'https://images.unsplash.com/photo-1441984904996-e0b6ba687e04?w=600'
    
    def get_sizes_list(self):
        """Return sizes as a list"""
        if self.sizes:
            return [s.strip() for s in self.sizes.split(',')]
        return []
    
    def get_colors_list(self):
        """Return colors as a list"""
        if self.colors:
            return [c.strip() for c in self.colors.split(',')]
        return []

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/gallery/')
    alt_text = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - Image"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=10, blank=True)
    color = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

    @property
    def total_price(self):
        return self.product.final_price * self.quantity

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=100, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Shipping information
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order {self.order_number} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10, blank=True)
    color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.order.order_number} - {self.product.name}"

    @property
    def total_price(self):
        return self.price * self.quantity
