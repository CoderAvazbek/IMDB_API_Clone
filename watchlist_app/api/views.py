from rest_framework.response import Response
from watchlist_app.serializers import MovieSerializer
from watchlist_app.models import Movie
from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def movie_list(request):
    
    if request.method == "GET":
        movies = Movie.objects.all()
        srl_movies = MovieSerializer(movies, many=True)
        return Response(srl_movies.data)
    
    if request.method == "POST":
        srl_data = MovieSerializer(data=request.data)
        if  srl_data.is_valid():
            srl_data.save()
            return Response(srl_data.data)
        else:
            return Response(srl_data.errors)

@api_view(["GET"])
def detail_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    srl_movies = MovieSerializer(movie)
    return Response(srl_movies.data)
    