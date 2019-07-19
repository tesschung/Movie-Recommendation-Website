'''
import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv


# 현재부터 과거까지의 원하는 주간을 입력합니다
def week(week_number): # 원하는 만큼의 주간을 입력하세요.
    week_list = []
    for week in range(1, week_number+1):
        targetDt = datetime(2019, 7, 13) - timedelta(weeks=week) 
        targetDt = targetDt.strftime('%Y%m%d') # yyymmdd
        week_list.append(targetDt)
    return week_list

api_url_list = []
for targetDt in week(50): ### data parsing 조절
    key = config('API_KEY')
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    weekGb = '0' # 우리가 원하는 주간으로 가져온다.

    # 우리가 원하는 multiMovieYn, repNationCd, wideAreaCd는 이미 default값이므로 따로 지정하지 않습니다.
    api_url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb={weekGb}'
    api_url_list.append(api_url)

with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
    # 저장할 필드의 이름을 미리 지정한다.
    fieldnames = ('movieCd', 'movieNm', 'audiCnt')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # 필드 이름을 csv 파일 최상단에 작성한다.
    writer.writeheader() # 최상단 카테고리

        # 원하는 주간내의 data들을 json으로 parsing하여 가져옵니다.
    for api_url in api_url_list:
        response = requests.get(api_url) # 200
        data = response.json()
        #pprint(data) # 데이터를 잘 가져왔는지 확인 합니다.

        # 가져온 data에서 원하는 정보만 수집합니다.
        weeklyBoxOfficeLists = data.get('boxOfficeResult').get('weeklyBoxOfficeList')
        #print(weeklyBoxOfficeList)

        weeklyBoxOfficeDicts = {}

        for weeklyBoxOfficeList in weeklyBoxOfficeLists:
            if weeklyBoxOfficeList.get('movieCd') not in weeklyBoxOfficeDicts:

                weeklyBoxOfficeDicts['movieCd'] = weeklyBoxOfficeList.get('movieCd')
                weeklyBoxOfficeDicts['movieNm'] = weeklyBoxOfficeList.get('movieNm') 
                weeklyBoxOfficeDicts['audiCnt'] = weeklyBoxOfficeList.get('audiCnt')

                writer.writerow(weeklyBoxOfficeDicts)
'''

import csv
import datetime
import requests
from decouple import config


key = config('API_KEY')
movie_data = {}
for i in range(51):
    targetDt = datetime.datetime(2019, 7, 13) - datetime.timedelta(weeks=i)
    targetDt = targetDt.strftime('%Y%m%d')
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0'
    response = requests.get(api_url).json()

    for movie in response['boxOfficeResult']['weeklyBoxOfficeList']:
        if movie.get('movieCd') not in movie_data:
            movie_data[movie.get('movieCd')] = {
                                                'movieCd': movie.get('movieCd'),
                                                'audiAcc': movie.get('audiAcc'),
                                                'movieNm': movie.get('movieNm')
                                            }

with open('boxoffice.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['movieCd', 'audiAcc', 'movieNm'] 
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in movie_data.values():
        csv_writer.writerow(item)
