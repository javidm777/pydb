# Generated by Django 4.2.4 on 2023-08-09 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_products_company_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
