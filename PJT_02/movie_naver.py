import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv
import time

# pjt_01 폴더에서 csv파일 읽어와서 reader에 넣고, moives <= 모든 영화 데이터를 받을 딕셔너리. 키값은 영화제목으로 할 예정
with open('movie.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

#새로운 csv파일을 만들어서 헤더들만 넣어놓자. 나중에 영화데이터를 추가할때 'w'(덮어쓰기)대신 'a'(데이터 추가)로 넣는데. 그럼 테스트할때마다 줄이 추가되기때문에
#테스트할때 csv를 처음부터 만들기위해서 따로넣어놓습니다.
    with open('movie_naver.csv', 'w', newline='', encoding='utf-8') as f:

        fieldnames = ('movieCd', 'title', 'link', 'image', 'userRating')
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader() 

        for row in reader:

            movieCd = row['영화 대표코드']
            query = row['영화명(국문)']
            openDt = row['개봉연도']
            openDt = openDt[:4]

            BASE_URL = config('BASE_URL')
            CLIENT_ID = config('CLIENT_ID')
            CLIENT_SECRET = config('CLIENT_SECRET')

            params = {

                'query':query
                
                }

            HEADERS = {
                
                'X-Naver-Client-Id' : CLIENT_ID,
                'X-Naver-Client-Secret' : CLIENT_SECRET, #trailing convention

            }

            API_URL = f'{BASE_URL}?'
            response = requests.get(API_URL, params=params, headers=HEADERS).json()

            movie_naver_dict = {}

            items = response.get('items')
            pprint(items)
            
            try:
                for item in items:

                    if item['pubDate'] == openDt: #pubDate 최신일자로 검증 'pubDate': '2018'
                        if item['image'] != '': #영화 썸네일 이미지의 URL 이 없는 경우 저장하지 않습니다.
                            movie_naver_dict['movieCd'] = movieCd
                            movie_naver_dict['title'] = item['title']
                            movie_naver_dict['link'] = item['link']
                            movie_naver_dict['image'] = item['image']
                            movie_naver_dict['userRating'] = item['userRating']
                            writer.writerow(movie_naver_dict)

                    else:
                        continue

            except TypeError:
                continue
     

            
