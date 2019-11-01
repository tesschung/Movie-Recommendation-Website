# Project_08: 



### 목표
- API 요청에 대한 이해
- RESTful API 서버 구축
- API 문서화



### 준비 사항

- (필수) Python Web Framework
- Django 2.2.x
- Python 3.7.x



### 요구 사항



#### 데이터베이스 설계
db.sqlite3 에서 테이블 간의 관계

필드명 자료형 설명
id Interger Primary Key
title String 영화명
audience Integer 누적 관객수
poster_url String 포스터 이미지 URL
description Text 영화 소개
genre_id Integer Genre의 Primary Key(id 값)
movies_movies

```python
class Movie(models.Model):
title = models.CharField(max_length=50)
audience = models.IntegerField()
poster_url = models.CharField(max_length=50)
description = models.TextField()
# genre Movie에 접근할 수 있도록 
# related_name으로 다리를 만들어준다.
genre = models.ForeignKey(Genre, on_delete=models.CASCADE, 		related_name='movies')
```


필드명 자료형 설명
id Interger Primary Key
name String 장르 구분
movies_genres
movies_reviews

```python
class Genre(models.Model):
name = models.CharField(max_length=50)
```

필드명 자료형 설명
id Integer Primary Key
content String 한줄평(평가 내용)
score Integer 평점
movie_id Integer Movie의 Primary Key(id 값)
user_id Integer User의 Primary Key(id 값)

```python
class Review(models.Model):
content = models.CharField(max_length=200)
score = models.IntegerField()
# ForeignKey로 엮어준다.
movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
user = models.ForeignKey(User, on_delete=models.CASCADE)
```



models.py 전체 코드

```python
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=50)
    description = models.TextField()
    # genre Movie에 접근할 수 있도록 
    # related_name으로 다리를 만들어준다.
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')

class Review(models.Model):
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    # ForeignKey로 엮어준다.
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



```



#### Seed Data 반영

주어진 movie.json 과 genre.json 을 movies/fixtures/ 디렉토리로 이동

- fixtures 파일 생성 후
- movie.json  genre.json 추가

아래의 명령어를 통해 반영

```bash
$ python manage.py loaddata genre.json
Installed 11 object(s) from 1 fixture(s)
$ python manage.py loaddata movie.json
Installed 10 object(s) from 1 fixture(s)
```

admin.py 에 Genre 와 Movie 클래스를 등록 후, 

/admin 을 통해 실제로 데이터베이스에 반영되었는지 확인
```bash
$ python manage.py createsuperuser
```






#### movies API
​    아래와 같은 API 요청을 보낼 수 있는 서버를 구축
​    허용된 HTTP 요청을 제외하고는 모두 405 Method Not Allowed를 응답



urls.py 작성

```python
from django.urls import path 
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# get_schema_view로 전달 받음
schema_view = get_schema_view(
    openapi.Info(
        title='Movie API',
        default_version='v1',
        description='영화 관련 API 서비스입니다.',
        terms_of_service='https://www.google.com/policies/terms/',
    )
)

app_name = 'movies'
# /api/v1/
urlpatterns = [
    # GET
    path('genres/', views.genre_list, name='genres_list'), 
    # GET # error
    path('genres/<int:genre_pk>/', views.genre_detail, name='genre_detail'),

    # GET
    path('movies/', views.movie_list, name='movie_list'), 
    # GET
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    
    # POST
    path('movies/<int:movie_pk>/scores/', views.movie_score, name='movie_score'),

    # GET, PUT, DELETE
    path('scores/<int:score_pk>/', views.score_list, name='score_list'),

    path('docs/', schema_view.with_ui('redoc'), name='api_docs'), # ui가 있는 상태에서 진행
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger')
]
```



serializer.py 생성 후 작성

```python
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
```





views.py 작성

```python
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
```

