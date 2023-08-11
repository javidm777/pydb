from django.db import models


# Create your models here.

class ProductType(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    crate_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    INTEGER = 1
    STRING = 2
    FLOAT = 3
    ATTRIBUTE_TYPE_FIELDS = (
        (INTEGER, 'integer'),
        (STRING, 'string'),
        (FLOAT, 'flaot'),
    )

    title = models.CharField(max_length=50)
    product_type = models.ForeignKey(
        ProductType, on_delete=models.PROTECT, related_name='attribute')

    attribute_type = models.PositiveSmallIntegerField(
        default=INTEGER, choices=ATTRIBUTE_TYPE_FIELDS)
    crate_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children', null=True,
    blank=True)
    crate_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children', null=True,
    blank=True)
    crate_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_type = models.ForeignKey(
        ProductType, on_delete=models.PROTECT, related_name='products')
    upc = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='products')
    crate_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='attribute_value')
    value = models.CharField(max_length=50)
    attribute = models.ForeignKey(
        ProductAttribute, on_delete=models.PROTECT, related_name='values')
    crate_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product}({self.attribute}){self.value}'


