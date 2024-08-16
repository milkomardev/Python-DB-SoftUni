# Generated by Django 4.2.4 on 2023-10-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='works_full_time',
            field=models.BooleanField(),
        ),
    ]
