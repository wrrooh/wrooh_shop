from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'slug', 'created']
    list_filter = ['created']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'available', 'created']
    list_filter = ['available', 'created', 'category']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}