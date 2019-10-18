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

