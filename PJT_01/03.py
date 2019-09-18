import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv

#영화인 목록에 접근하여 peopleCd를 가져온다.
with open('movie.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    with open('director_temp.csv', 'w', newline='', encoding='utf-8') as f:
    # 저장할 필드의 이름을 미리 지정한다.
        fieldnames = ('peopleCd', 'peopleNm', 'filmoNames')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # 필드 이름을 csv 파일 최상단에 작성한다.
        writer.writeheader() # 최상단 카테고리
        for row in reader:
            peopleNm = row['peopleNm'] #peopleNm

            #print(peopleNm) #잘나옴
            base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json'
            key = config('API_KEY')
            api_url = f'{base_url}?key={key}&peopleNm={peopleNm}'

            response = requests.get(api_url)
            #print(response)

            data = response.json()

            peopleListResultList = data.get('peopleListResult')
            
            # pprint(peopleListResultList)

            searchPeopleList = {}

            peopleList = peopleListResultList.get('peopleList')[0]
            # pprint(peopleList)

            peopleCd = peopleList.get('peopleCd')
            peopleNm = peopleList.get('peopleNm')
            filmoNames = peopleList.get('filmoNames')

            searchPeopleList['peopleCd'] = peopleCd
            searchPeopleList['peopleNm'] = peopleNm
            searchPeopleList['filmoNames'] = filmoNames

            # print(searchPeopleList)
        

            writer.writerow(searchPeopleList)
