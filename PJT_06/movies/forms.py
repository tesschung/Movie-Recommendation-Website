from django import forms
from .models import Movie, Comment

# 사용자로부터 comment를 받을 form에 대한 template를 생성
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