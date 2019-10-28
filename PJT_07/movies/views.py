from django.shortcuts import render, redirect, get_object_or_404
from .models import Comments, Movies
from .forms import CommentForm, MoviesForm
from django.views.decorators.http import require_POST, require_GET


@require_GET
def index(request):
    movies = Movies.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def create(request):
    if request.method == 'POST':
        movie_form = MoviesForm(request.POST)
        if movie_form.is_valid():
            
            movie = movie_form.save(commit=False)
            movie.user=request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        movie_form = MoviesForm()
    return render(request, 'movies/create.html', {'movie_form':movie_form})


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    comment_form = CommentForm()
    return render(request, 'movies/detail.html', {'movie':movie, 'comment_form':comment_form})


@require_POST
def delete(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    movie.delete()
    return redirect('movies:index')


def update(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    if request.method == 'POST':
        movie_form = MoviesForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movies:detail', movie_pk)
    else:
        movie_form = MoviesForm(instance=movie)
    return render(request, 'movies/update.html', {'movie_form': movie_form, 'movie_pk':movie_pk})
    
@require_POST
def review(request, movie_pk):
    comment_form = CommentForm(request.POST)
    if request.user.is_authenticated:
        if comment_form.is_valid():
            
            comment = comment_form.save(commit=False)
            comment.movie_id = movie_pk
            comment.user = request.user
            comment_form.save()
    return redirect('movies:detail', movie_pk)

@require_POST
def comments_delete(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comments, pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)


def like(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movies, pk=movie_pk)
    if user in movie.like_users.all():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)

    return redirect('movies:detail', movie_pk)


def like_list(request):

    return render(request, 'movies/like_list.html')