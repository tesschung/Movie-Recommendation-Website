from django.urls import path 
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# get_schema_view로 전달 받음
schema_view = get_schema_view(
    openapi.Info(
        title='Movie API',
        default_version='v1',
        description='영화 관련 API 서비스입니다.',
        terms_of_service='https://www.google.com/policies/terms/',
    )
)

app_name = 'movies'
# /api/v1/
urlpatterns = [
    # GET
    path('genres/', views.genre_list, name='genres_list'), 
    # GET # error
    path('genres/<int:genre_pk>/', views.genre_detail, name='genre_detail'),

    # GET
    path('movies/', views.movie_list, name='movie_list'), 
    # GET
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    
    # POST
    path('movies/<int:movie_pk>/scores/', views.movie_score, name='movie_score'),

    # GET, PUT, DELETE
    path('scores/<int:score_pk>/', views.score_list, name='score_list'),

    path('docs/', schema_view.with_ui('redoc'), name='api_docs'), # ui가 있는 상태에서 진행
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger')
]