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

            
        

