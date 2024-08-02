from django.urls import path
from .views import movie_list, detail_movie


urlpatterns = [
    path("list/", movie_list, name="list"),
    path('<int:pk>/', detail_movie, name="detail_movie")
] 