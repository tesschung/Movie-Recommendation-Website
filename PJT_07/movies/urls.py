from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/review/', views.review, name='review'),
    path('<int:movie_pk>/comments_delete/<int:comment_pk>', views.comments_delete, name='comments_delete'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('like_list/', views.like_list, name='like_list'),
]
