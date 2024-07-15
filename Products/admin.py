# products/admin.py

from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'status', 'is_active', 'created_at', 'updated_at')
    list_filter = ('category', 'status', 'is_active')
    search_fields = ('name', 'description', 'sku')
    actions = ['make_live', 'make_deleted']

    def make_live(self, request, queryset):
        queryset.update(status=1)
    make_live.short_description = "Mark selected products as live"

    def make_deleted(self, request, queryset):
        queryset.update(status=0)
    make_deleted.short_description = "Mark selected products as deleted"

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
