from django.contrib import admin
from catalogue.models import Category, Brand, Product,\
    ProductType, ProductAttributeValue


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'upc',
        'title',
        'product_type',
        'category',
        'brand',
    ]
    search_fields = ['upc', 'title', 'category__name', 'brand__name']
    list_display_links = ['title', 'upc']


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)
admin.site.register(ProductAttributeValue)
