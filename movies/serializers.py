from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('Movie release date cannot be before 1990.')
        return value
    
    def validate_synopsis(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Movie synopsis cannot be longer than 200 characters.')
        return value
