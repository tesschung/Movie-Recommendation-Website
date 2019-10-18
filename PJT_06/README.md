

## Project_06: 

## Django

`python 3.7`

[TOC]

#### Overview

- Python Web Framework를 통한 데이터 조작

- Object Relational Mapping에 대한 이해

- Template Variable을 활용한 Template 제작

- Static 파일 관리



#### Requirements

1. (필수) Python Web Framework - Django
2. (필수) Python Web Framework 사용을 위한 환경 설정 가상환경 Python 3.7+



#### Goal

- 영화 정보 홈페이지
- 개별 영화에 대한 영화평 생성, 수정, 삭제 홈페이지



#### Development Method

models.py 정의

```python
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

    class __str__(self):
        return f'{self.title}: {self.description}'
    
# 개별 영화에 대한 한줄평
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=50)
    score = models.IntegerField()
```



forms.py

```python
from django import forms
from .models import Movie, Comment

# 사용자로부터 comment를 받을 form에 대한 template를 생성
# 미리 form에 정의를 함으로써 재활용성을 높인다.
class MovieForm(forms.ModelForm):
    title = forms.CharField(
        max_length=50,
        label='제목',
        widget=forms.TextInput(
        )
    )
    title_en = forms.CharField(
        max_length=50,
        label='영문 제목',
        widget=forms.TextInput(
        )
    )
    audience = forms.IntegerField(
        label='관객수',
        widget=forms.NumberInput()
    )
    open_date = forms.DateField(
        label='개봉 날짜',
        widget=forms.DateInput,
        input_formats=[
            '%Y-%m-%d',
            '%m/%d/%Y',
            '%m/%d/%y',
            '%Y/%m/%d',
            '%y/%m/%d'
            ]
    )
    genre = forms.CharField(
        max_length=20,
        label='장르',
        widget=forms.TextInput,
    )
    watch_grade = forms.CharField(
        max_length=20,
        label='관람 등급',
        widget=forms.TextInput,
    )
    score = forms.FloatField(
        label='평점',
        widget=forms.NumberInput,
    )
    poster_url = forms.CharField(
        label='포스터 URL',
        widget=forms.TextInput,
    )
    description = forms.CharField(
        label='상세 설명',
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'cols': 30,
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['movie']
```



views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    commentform = CommentForm()
    comments = movie.comments.all()
    context = {'movie': movie, 'commentform': commentform, 'comments': comments}
    return render(request, 'movies/detail.html', context)

def create(request):
    if request.method == 'POST':
        movieform = MovieForm(request.POST)
        if movieform.is_valid():
            movieform.save()
            return redirect('movies:index')

    else:
        movieform = MovieForm()
    context = {'movieform':movieform}
    return render(request, 'movies/create.html', context)

def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        movieform = MovieForm(request.POST, instance=movie)
        if movieform.is_valid():
            movieform.save()    
            return redirect('movies:detail', movie_pk)

    # GET : Update 를 하기위한 Form을 제공하는 페이지
    else: # POST가 아니라 GET이라면,
        movieform = MovieForm(instance=movie)
    context = {
        'movie' : movie,
        'movieform': movieform,
    }
    return render(request, 'movies/update.html', context)

def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.delete()
    return redirect('movies:index')

def reviews(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            # 위의 옵션을 이용해 모델 클래스로 생성한 인스턴스 객체만 반영하고, DB에는 반영하지 않는다.
            content = commentform.cleaned_data.get('content')
            score = commentform.cleaned_data.get('score')
            comment = Comment()
            comment.content = content
            comment.score = score
            comment.movie = movie
            comment.save()
            # 생성한 다음 Movie detail page로 redirect
            return redirect('movies:detail', movie_pk)

def review_delete(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)

```

