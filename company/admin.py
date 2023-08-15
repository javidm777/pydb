from django.contrib import admin
from django.contrib.admin import register
from company.models import Company, Product


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'Number', 'country')
    list_display_links = ('name', 'Number', 'country')


admin.site.register(Company, CompanyAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'upc', 'title')


admin.site.register(Product, ProductAdmin)