from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)
    audience = models.IntegerField()
    open_data = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    # class Meta:
    #     ordering = ['-pk', ]
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='movie_users'
        )

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_movies'
    )

    
class Comments(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    content = models.CharField(max_length=40)
    score = models.IntegerField()
    


