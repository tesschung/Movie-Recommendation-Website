import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv
import time

with open('data2.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = row['movieNm']
        title_en = row['movieNmEn']
        audience = row['audiAcc']
        open_date = row['openDt']
        genre = row['GenreNm']
        watch_grade = row['watchGradeNm']
        score = row['Score']
        poster_url = row['Naver']
        description = row['Description']

        save = 'http://127.0.0.1:8000/movies/create/'
        query = f'?title={title}&title_en={title_en}&audience={audience}&open_date={open_date}&genre={genre}&watch_grade={watch_grade}&score={score}&poster_url={poster_url}&description={description}'
        response = requests.get(save+query)
