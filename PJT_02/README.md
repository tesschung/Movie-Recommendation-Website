

## Project_02: 

## 파이썬을 활용한 데이터 수집 II

`python 3.7`

[TOC]



#### Overview

저번에 가져온 데이터를 통해

포스터 가져오는 방법



#### Requirements

활용 API 정보

https://developers.naver.com/apps/#/register?defaultScope=search

Naver Developer의 오픈API



https://developers.naver.com/docs/search/movie/

**HTTP Header**에 애플리케이션 등록 시 발급받은 [Client ID와 Client Secret 값을 같이 전송]



#### Module

`requests`



#### Goal

API 요청을 통한 데이터 수집 및 파일 저장
Python을 통한 JSON 및 이미지 파일 조작
API 활용을 통해 데이터를 수집하고 내가 원하는 형태로 가공한다.
영화평점서비스(예- watcha)에 필요한 추가 데이터를 프로그래밍을 통해 수집한다.



#### Developement Method

1. 네이버 영화 검색 API - movie_naver.py
    지난 프로젝트(파이썬을 활용한 데이터 수집 I)에서 얻은 영화명(국문)을 바탕으로 네이버 영화 검색 API를 통해
    추가적인 데이터를 수집합니다. 해당 데이터는 향후 영화평점서비스에서 기준 평점 및 영화 포스터 썸네일로 활
    용될 것입니다.

  https://openapi.naver.com/v1/search/movie.json

  GET

요청
**영화명**을 통해 요청합니다.  query

응답
영화별로 다음과 같은 내용을 저장합니다.



- [x]  영진위 영화 대표코드 (.csv에서 가져와서 같이 저장) **영화명(국문)**    **movieNm**
- [x]  하이퍼텍스트 **link** 
- [x]  영화 썸네일 이미지의 URL ,  **image**
- [x] 유저 평점 **userRating**

영화 썸네일 이미지의 URL 이 없는 경우 저장하지 않습니다.

-> 없으면 저장하지 않음을 if~~in 으로 확인

해당 결과를 movie_naver.csv에 저장합니다.

```python
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

            HEADERS = {
                'X-Naver-Client-Id' : CLIENT_ID,
                'X-Naver-Client-Secret' : CLIENT_SECRET, #trailing convention
            }

            API_URL = f'{BASE_URL}?query={query}'
            response = requests.get(API_URL, headers=HEADERS).json()

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
```



2. 영화 포스터 이미지 저장 - movie_image.py

   앞서 네이버 영화 검색 API를 통해 얻은 **이미지 URL에 요청을 보내 실제 이미지 파일**로 저장합니다. 

해당 데이터는 향후 영화 목록에서 포스터 이미지로 사용될 것입니다.

요청
**영화 썸네일 이미지의 URL**

응답
응답 받은 결과를 **파일로 저장**합니다. 

반드시 **wb 옵션으로 저장하시기** **바랍니다.**
저장되는 파일명은 **images** 폴더 내에 **영진위 영화 대표코드.jpg** 입니다.



```python
import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv
import time

with open('movie_naver.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        thumb_url = row['image']
        pprint(thumb_url)
        title = row['movieCd']
        with open(f'images/{title}.jpg', 'wb') as f: # wb: write binary
            response = requests.get(thumb_url) # url을 요청을 보내서 파일을 응답받는다.
            print(response)
            f.write(response.content)
```



#### Start

기본요청 URL

https://openapi.naver.com/v1/search/movie.json