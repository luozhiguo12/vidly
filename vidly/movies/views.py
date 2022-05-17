from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie
# from django.shortcuts import render


def index(request):
    # Movie.objects.filter(release_year=1984)

    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(id=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404('Movie does not exist')
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})