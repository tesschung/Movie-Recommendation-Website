from django.shortcuts import render
from .models import Movie

# Create your views here.

# 영화목록 
def movielist(request):
    movielist = Movie.objects.all()
    context = {
        'movielist': movielist,
    }
    return render(request, 'movies/movielist.html', context)

# 영화 정보 Form 생성
def new(request):
    return render(request, 'movies/new.html')

# 영화 정보 DB 저장
def create(request):
     # 사용자가 form 에서 전달한 정보를 꺼낸다
    title = request.GET.get('title')
    title_en = request.GET.get('title_en')
    audience = request.GET.get('audience')
    open_date = request.GET.get('open_date')
    genre = request.GET.get('genre')
    watch_grade = request.GET.get('watch_grade')
    score = request.GET.get('score')  
    poster_url = request.GET.get('poster_url')  
    description = request.GET.get('description') 


    # 해당 정보를 Movie 모델을 이용하여 새롭게 데이터를 저장한다.
    movie = Movie()

    movie.title = title
    movie.title_en = title_en
    movie.audience = audience
    movie.open_date = open_date
    movie.genre = genre
    movie.watch_grade = watch_grade
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description

    movie.save()
    # 사용자에게 저장이 완료되었다는 페이지를 보여준다.
    return render(request, 'movies/create.html')

def detail(request, movie_pk): # pk를 받은 것
    movies = Movie.objects.filter(pk=movie_pk)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/detail.html', context)

def delete(request, movie_pk):
    movies = Movie.objects.filter(pk=movie_pk)
    movies.delete()
    return render(request, 'movies/delete.html')

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.title = request.GET.get('title')
    movie.title_en = request.GET.get('title_en')
    movie.audience = request.GET.get('audience')
    movie.open_date = request.GET.get('open_date')
    movie.genre = request.GET.get('genre')
    movie.watch_grade = request.GET.get('watch_grade')
    movie.score = request.GET.get('score')  
    movie.poster_url = request.GET.get('poster_url')  
    movie.description = request.GET.get('description') 
    movie.save()

    context = {
        'title': movie.title
    }
    
    return render(request, 'movies/update.html', context)

def edit(request, movie_pk):
    context = {
        'movie_pk': movie_pk
    }

    return render(request, 'movies/edit.html', context)