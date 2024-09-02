import os
import django
from django.db.models import Q, Count, Avg, F

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ''

    query = Q()
    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)
    if search_name and search_nationality:
        query = query_name & query_nationality
    elif search_name:
        query = query_name
    else:
        query = query_nationality

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ''

    result = []

    for d in directors:
        result.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")

    return '\n'.join(result)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()
    if director is None:
        return ''

    return f"Top Director: {director.full_name}, movies: {director.movies_count}."


def get_top_actor():
    top_actor = (Actor.objects
                 .annotate(movies_count=Count('movies'), movies_average_rating=Avg('movies__rating'))
                 .order_by('-movies_count', 'full_name')
                 .first()
                 )

    if not top_actor or not Movie.objects.all():
        return ''

    movies = [m.title for m in top_actor.movies.all()]

    return (f"Top Actor: {top_actor.full_name},"
            f" starring in movies: {', '.join(movies)}, "
            f"movies average rating: {top_actor.movies_average_rating:.1f}")


def get_actors_by_movies_count():
    actors = (Actor.objects.prefetch_related('actors_movies')
              .annotate(movies_count=Count('actors_movies'))
              .filter(movies_count__gt=0)
              .order_by('-movies_count', 'full_name')
              )[:3]

    if not actors:
        return ''

    result = []

    for a in actors:
        result.append(f"{a.full_name}, participated in {a.movies_count} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    movie = (Movie.objects
             .select_related('starring_actor')
             .prefetch_related('actors')
             .filter(is_awarded=True)
             .order_by('-rating', 'title')
             .first()
             )

    if not movie:
        return ''

    cast = [a.full_name for a in movie.actors.order_by('full_name')]

    return (f"Top rated awarded movie: {movie.title}, "
            f"rating: {movie.rating:.1f}. "
            f"Starring actor: {movie.starring_actor.full_name if movie.starring_actor else 'N/A'}. "
            f"Cast: {', '.join(cast)}.")


def increase_rating():
    movies = (Movie.objects
              .filter(is_classic=True, rating__lt=10)
              .update(rating=F('rating') + 0.1)
              )

    if not movies:
        return "No ratings increased."

    return f"Rating increased for {movies} movies."


print(increase_rating())