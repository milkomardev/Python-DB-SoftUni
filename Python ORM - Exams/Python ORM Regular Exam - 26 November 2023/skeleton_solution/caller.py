import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review
from django.db.models import Q, F, Count, Avg, Sum, Max


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ''

    query = Q()
    query_name = Q(full_name__icontains=search_name)
    query_email = Q(email__icontains=search_email)

    if search_name and search_email:
        query = query_name & query_email
    elif search_name:
        query = query_name
    else:
        query = query_email

    authors = Author.objects.filter(query).order_by('-full_name')

    if not authors:
        return ''

    result = []

    for a in authors:
        result.append(f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}")

    return '\n'.join(result)


def get_top_publisher():
    author = ((Author.objects.get_authors_by_article_count())
              .filter(articles_count__gt=0)
              .first()
              )

    if not author:
        return ''

    return f"Top Author: {author.full_name} with {author.articles_count} published articles."


def get_top_reviewer():
    reviewer = (Author.objects
                .annotate(reviews_count=Count('reviews'))
                .filter(reviews_count__gt=0)
                .order_by('-reviews_count', 'email')
                .first()
                )

    if not reviewer:
        return ''

    return f"Top Reviewer: {reviewer.full_name} with {reviewer.reviews_count} published reviews."


def get_latest_article():
    if not Article.objects.all():
        return ''

    article = (Article.objects
               .prefetch_related('authors')
               .annotate(reviews_count=Count('reviews'), sum_reviews_rating=Sum('reviews__rating'))
               .order_by('-published_on')
               .first()
               )

    if article.reviews_count == 0:
        avg_reviews_rating = 0
    else:
        avg_reviews_rating = article.sum_reviews_rating / article.reviews_count

    authors_names = ', '.join([a.full_name for a in article.authors.all().order_by('full_name')])

    return (f"The latest article is: {article.title}. "
            f"Authors: {authors_names}. "
            f"Reviewed: {article.reviews_count} times. Average Rating: {avg_reviews_rating:.2f}.")


def get_top_rated_article():
    if Review.objects.all().count() == 0:
        return ''

    top_review = (Review.objects.order_by('-rating', 'article__title').first())
    reviews = Review.objects.filter(article=top_review.article).aggregate(avg_rating=Avg('rating'))
    reviews_count = Review.objects.filter(article=top_review.article).count()

    if reviews_count == 0:
        avg_rating = 0
    else:
        avg_rating = reviews['avg_rating']

    return (f"The top-rated article is: {top_review.article.title}, "
            f"with an average rating of {avg_rating:.2f}, "
            f"reviewed {reviews_count} times.")


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    author = (Author.objects
              .filter(email__exact=email)
              .annotate(reviews_count=Count('reviews'))
              .filter(is_banned=False)
              ).first()

    if not author or not Author.objects.all():
        return "No authors banned."

    author.is_banned = True
    author.save()

    reviews_to_delete = Review.objects.filter(author=author)
    for review in reviews_to_delete:
        review.delete()

    return f"Author: {author.full_name} is banned! {author.reviews_count} reviews deleted."


# print(ban_author('Author2@Author2.Author2'))
# print(get_latest_article())
print(get_top_rated_article())
