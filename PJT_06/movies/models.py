from django.db import models

# 영화에 대한 정보
class Movie(models.Model):
    title = models.CharField(max_length=50)
    title_en = models.CharField(max_length=50, default='')
    audience = models.IntegerField(default=0)
    open_date = models.DateTimeField()
    genre = models.CharField(max_length=50, default='')
    watch_grade = models.CharField(max_length=50, default='')
    score = models.FloatField(default=0)
    poster_url = models.TextField(default='')
    description = models.TextField(default='')
    
# 개별 영화에 대한 한줄평
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=50)
    score = models.IntegerField()