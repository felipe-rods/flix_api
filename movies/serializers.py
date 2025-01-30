from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
    
    
    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        if rating:
            return round(rating, 1)
        return None
    
    
    def validate_synopsis(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError('Movie synopsis cannot be longer than 1000 characters.')
        return value
