# Generated by Django 4.2.4 on 2023-10-29 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_product_category_alter_product_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
