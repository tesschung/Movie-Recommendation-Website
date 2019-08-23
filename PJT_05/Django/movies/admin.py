from django.contrib import admin
from .models import Movie

# Register your models here.
# @admin.register(Movie)  # admin site에 Article을 register
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'title_en', 'audience', 'open_date', 'genre', 'watch_grade', 'score', 'poster_url', 'description')

admin.site.register(Movie)
