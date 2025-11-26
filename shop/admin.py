from django.contrib import admin
from .models import Category, Product, ProductImage, Cart, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active']
    ordering = ['name']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    fields = ['image', 'alt_text']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'discount_price', 'quantity', 'is_featured', 'is_active', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'quantity', 'is_featured', 'is_active']
    ordering = ['-created_at']
    inlines = [ProductImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'category')
        }),
        ('Pricing', {
            'fields': ('price', 'discount_price')
        }),
        ('Inventory', {
            'fields': ('quantity', 'sizes', 'colors')
        }),
        ('Media', {
            'fields': ('photo',)
        }),
        ('Status', {
            'fields': ('is_featured', 'is_active')
        }),
    )

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'alt_text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['product__name', 'alt_text']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'size', 'color', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'product__name']
    ordering = ['-created_at']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price', 'size', 'color']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'full_name', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['order_number', 'user__username', 'full_name', 'email', 'phone']
    list_editable = ['status']
    ordering = ['-created_at']
    inlines = [OrderItemInline]
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'total_amount', 'status')
        }),
        ('Customer Details', {
            'fields': ('full_name', 'email', 'phone')
        }),
        ('Shipping Address', {
            'fields': ('address', 'city', 'state', 'pincode')
        }),
    )
    
    readonly_fields = ['order_number', 'user', 'total_amount']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'size', 'color']
    list_filter = ['order__created_at']
    search_fields = ['order__order_number', 'product__name']
