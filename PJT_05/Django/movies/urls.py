from django.urls import path
from . import views

# movies/___
urlpatterns = [
    path('<int:movie_pk>/edit/', views.edit),
    path('<int:movie_pk>/delete/', views.delete),
    path('<int:movie_pk>/update/', views.update),

    path('new/', views.new),
    path('create/', views.create),
    path('<int:movie_pk>/', views.detail),
    path('', views.movielist),
]
