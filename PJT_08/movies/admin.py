from django.contrib import admin
from .models import *

# admin 페이지에 model 정보 반영

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)