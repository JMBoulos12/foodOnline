# Generated by Django 5.0.1 on 2024-01-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_alter_vendor_vendor_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_license',
            field=models.ImageField(upload_to='vendor/license'),
        ),
    ]
