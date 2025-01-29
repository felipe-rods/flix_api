from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView
from actors.views import ActorListCreateView, ActorRetrieveUpdateDestroyView
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    
    path('actors/', ActorListCreateView.as_view(), name='actor-list-create'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),

    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view')
]
