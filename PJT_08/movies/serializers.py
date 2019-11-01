from rest_framework import serializers
from .models import *

# Genre
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', )

# Movie
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'audience', 'poster_url', 'description', 'genre_id', )

class GenreDetailSerializer(GenreSerializer):
    movies = MovieSerializer(many=True)
    class Meta(GenreSerializer.Meta):
        # 여기서 movies는 related_name
        fields = GenreSerializer.Meta.fields + ('movies', )


# Score
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # movie_id , user_id 중요
        fields = ('id', 'content', 'score', 'movie_id', 'user_id', )