from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from reviews.models import Review


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    
    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_rating = Review.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']

        return response.Response(data={
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews': total_reviews,
                'average_rating': round(average_rating, 2) if average_rating else 0,
        }, status=status.HTTP_200_OK)
