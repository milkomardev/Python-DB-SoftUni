# Generated by Django 4.2.4 on 2023-10-23 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='estimated_hours',
            field=models.FloatField(blank=True, null=True, verbose_name='Estimated Hours'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Start Date'),
        ),
    ]
