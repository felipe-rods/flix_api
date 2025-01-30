from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rating(self, obj):
        reviews = obj.reviews.all()

        if reviews:
            sum_reviews = 0
            for review in reviews:
                sum_reviews += review.rating
            reviews_count = reviews.count()
            return round(sum_reviews / reviews_count, 1)
        
        return None
    
    def validate_synopsis(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError('Movie synopsis cannot be longer than 1000 characters.')
        return value
