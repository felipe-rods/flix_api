from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreModelSerializer
from actors.serializers import ActorModelSerializer


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_synopsis(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError('Movie synopsis cannot be longer than 1000 characters.')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorModelSerializer(many=True)
    genre = GenreModelSerializer()
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rating', 'synopsis']

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        if rating:
            return round(rating, 1)
        return None
