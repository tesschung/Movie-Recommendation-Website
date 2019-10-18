from django.urls import path, include
from . import views
app_name = 'movies'
urlpatterns = [
    # 영화 정보 목록
    path('', views.index, name='index'),

    # 영화 정보 조회
    path('<int:movie_pk>/', views.detail, name='detail'),

    # 영화 정보 생성
    path('create/', views.create, name='create'),

    path('<int:movie_pk>/delete/', views.delete, name='delete'),

    path('<int:movie_pk>/update/', views.update, name='update'),

    path('<int:movie_pk>/reviews/', views.reviews, name='reviews'),

    path('<int:movie_pk>/<int:comment_pk>/review_delete/', views.review_delete, name='review_delete')
]
