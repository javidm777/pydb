# Generated by Django 4.2.4 on 2023-08-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
