import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv

with open('director_temp.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    with open('director.csv', 'w', newline='', encoding='utf-8') as f:
# 저장할 필드의 이름을 미리 지정한다.
        fieldnames = ('peopleCd', 'peopleNm', 'repRoleNm', 'movieNm')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # 필드 이름을 csv 파일 최상단에 작성한다.
        writer.writeheader() # 최상단 카테고리

        people = []

        for row in reader:
            peopleCd = row['peopleCd'] #peopleCd
            people.append(peopleCd)
        
        people = list(set(people)) #중복제거(동명이인살리기)
        
        for person in people:
            base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.json'
            key = config('API_KEY')
            api_url = f'{base_url}?key={key}&peopleCd={person}'

            response = requests.get(api_url)
            
            #print(response)

            data = response.json()
            #pprint(data)

            searchPeopleInfo = {}

            peopleInfo = data.get('peopleInfoResult').get('peopleInfo')

            
            #filmos = data.get('peopleInfoResult').get('peopleInfo').get('filmos')
            #pprint(peopleInfo)
            peopleCd = peopleInfo.get('peopleCd')
            #print(peopleCd)
            peopleNm = peopleInfo.get('peopleNm')
            repRoleNm = peopleInfo.get('repRoleNm')
            filmos = peopleInfo.get('filmos')[0] #filmo
            movieNm = filmos.get('movieNm')

            pprint(movieNm)

            searchPeopleInfo['peopleCd'] = peopleCd
            searchPeopleInfo['peopleNm'] = peopleNm
            searchPeopleInfo['repRoleNm'] = repRoleNm
            searchPeopleInfo['movieNm'] = movieNm #filmo

            writer.writerow(searchPeopleInfo)