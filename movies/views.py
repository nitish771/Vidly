from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie, Genre


def index(request):
    movies = Movie.objects.all()
    print(movies)
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/details.html', {'movie': movie})
