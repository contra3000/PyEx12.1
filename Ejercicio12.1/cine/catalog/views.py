from django.http import HttpResponse
from django.shortcuts import render
from . models import *

def saludo (request):
    return HttpResponse(Movie.director)


def index(request):
    directores = Director.objects.all()
    movies = Movie.objects.all()
    num_movies = Movie.objects.all().count()
    num_directors = Director.objects.all().count()
    num_genres = Genre.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'movies': movies,
            'directores': directores,
            'num_movies': num_movies,
            'num_directors': num_directors,
            'num_genres': num_genres
        }
    )
