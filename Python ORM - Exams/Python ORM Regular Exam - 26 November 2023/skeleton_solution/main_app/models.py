from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import AuthorManager


class Info(models.Model):
    content = models.TextField(
        validators=[MinLengthValidator(10)]
    )

    class Meta:
        abstract = True


class TimeStamp(models.Model):
    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        abstract = True


class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
    )

    email = models.EmailField(
        unique=True,
    )

    is_banned = models.BooleanField(
        default=False,
    )

    birth_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2005),
        ],
    )

    website = models.URLField(
        blank=True,
        null=True,
    )

    objects = AuthorManager()

    def __str__(self):
        return self.full_name


class Article(Info, TimeStamp):
    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = "Technology"
        SCIENCE = "Science"
        EDUCATION = "Education"

    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)],
    )

    category = models.CharField(
        max_length=10,
        choices=CategoryChoices.choices,
        default=CategoryChoices.TECHNOLOGY,
    )

    authors = models.ManyToManyField(
        Author,
        related_name='articles'
    )

    def __str__(self):
        return self.title


class Review(Info, TimeStamp):
    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0),
        ],
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
