from django.db import models


# Create your models here.


class Product(models.Model):
    object = None
    upc = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50, blank=True, )
    email = models.CharField(max_length=50, blank=True)
    Number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    country = models.CharField(blank=True)
    city = models.CharField(blank=True)
    product = models.ManyToManyField(Product, related_name='company')
    company_logo = models.ImageField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name
