from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import serializers
# Create your views here.



@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
    # id
    # name

@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)
    # id
    # movies -> id, title, audience, poster_url, description
    # name


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    # id
    # title
    # audience
    # poster_url
    # description
    # genre

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    # id
    # title
    # audience
    # poster_url
    # description
    # genre


@api_view(['POST'])
def movie_score(request, movie_pk):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk, user_id=1)
    return Response({'message':'작성되었습니다.'})
    

@api_view(['GET', 'PUT', 'DELETE'])
def score_list(request, score_pk):
    score = get_object_or_404(Review, pk=score_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(score)
        return Response(serializer.data) # 그냥 정보 가져오기

    elif request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data, instance=score)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'수정되었습니다.'})

    elif request.method == 'POST':
        score.delete()
        return Response({'message':'삭제되었습니다.'})
    # message
    # pass