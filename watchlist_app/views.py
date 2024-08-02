from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse, Http404

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        "Movies": list(movies.values())
    }
    return JsonResponse(data)

def detail_movie(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
        data = {
            "id": movie.id,
            "name": movie.name,
            "description": movie.description,
            "active": movie.active,
        }
        return JsonResponse(data)
    except Movie.DoesNotExist:
        Http404("Movie Does not found")