# Generated by Django 4.2.4 on 2023-08-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_rename_products_company_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='product',
            field=models.ManyToManyField(related_name='company', to='company.product'),
        ),
    ]
