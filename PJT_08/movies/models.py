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


