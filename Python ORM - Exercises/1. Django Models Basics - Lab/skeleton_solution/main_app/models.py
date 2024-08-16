from datetime import date

from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(
        max_length=30
        )

    email_address = models.EmailField(
        null=True
        )

    photo = models.URLField(
        null=True
    )

    birth_date = models.DateField(
        null=True, 
        blank=False
    )

    works_full_time = models.BooleanField()

    created_on = models.DateTimeField(
        auto_now_add=True
    )


class Department(models.Model):
    LOCATION_CHOICES = [
        ("Sofia", "Sofia"), 
        ("Plovdiv", "Plovdiv"), 
        ("Burgas", "Burgas"), 
        ("Varna", "Varna")
        ]

    code = models.CharField(
        max_length=4, 
        primary_key=True, 
        unique=True
    )

    name = models.CharField(
        max_length=50, 
        unique=True
    )

    employees_count = models.PositiveIntegerField(
        verbose_name="Employees Count", 
        default=1
    )

    location = models.CharField(
        max_length=20, 
        choices=LOCATION_CHOICES, 
        null=True
    )

    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False
    )



class Project(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True
    )

    description = models.TextField(
        null=True, 
        blank=True
    )

    budget = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True
    )

    duration_in_days = models.PositiveIntegerField(
        verbose_name="Duration in Days", 
        null=True, 
        blank=True
    )

    estimated_hours = models.FloatField(
        verbose_name="Estimated Hours", 
        null=True, 
        blank=True
    )

    start_date = models.DateField(
        verbose_name="Start Date", 
        default=date.today
    )

    created_on = models.DateTimeField(
        auto_now_add=True, 
        editable=False
    )

    last_edited_on = models.DateTimeField(
        auto_now=True, 
        editable=False
    )



