import requests
from pprint import pprint

CLIENT_ID='cKChcLTu0ZVdJ87qBOIJ'
CLIENT_SECRET='zp1mHpZH46'
BASE_URL='https://openapi.naver.com/v1/search/movie.json'

HEADERS = {
    'X-Naver-Client-Id' : CLIENT_ID,
    'X-Naver-Client-Secret' : CLIENT_SECRET
}

query = '자전차왕 엄복동'

API_URL = f'{BASE_URL}?query={query}'

response = requests.get(API_URL, headers=HEADERS).json()
pprint(response)