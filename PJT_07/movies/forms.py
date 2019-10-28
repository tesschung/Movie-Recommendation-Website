from django import forms
from .models import Movies, Comments

class MoviesForm(forms.ModelForm):
    title = forms.CharField(label='제목')
    title_en = forms.CharField(label='제목(영문)')
    audience = forms.IntegerField(label='누적관객수')
    open_data = forms.DateField(label='개봉일')
    genre = forms.CharField(label='장르')
    watch_grade = forms.CharField(label='관람등급')
    score = forms.FloatField(label='평점')
    poster_url = forms.CharField(label='포스터URL')
    description = forms.CharField(label='영화 소개', widget=forms.Textarea())
    class Meta:
        model = Movies
        fields = '__all__'
        exclude = ['user', 'like_users']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='한줄평', widget=forms.TextInput())
    score = forms.IntegerField(label='평점')
    class Meta:
        model = Comments
        fields = ['content', 'score', ]
