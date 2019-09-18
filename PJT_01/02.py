import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv

with open('boxoffice.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    with open('movie.csv', 'w', newline='', encoding='utf-8') as f:
    # 저장할 필드의 이름을 미리 지정한다.
        fieldnames = ('movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'watchGradeNm', 'openDt', 'showTm', 'genreNm', 'peopleNm', 'companyNm' )
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # 필드 이름을 csv 파일 최상단에 작성한다.
        writer.writeheader() # 최상단 카테고리

        for row in reader:
            movieCd = row['movieCd']
                #print(movieCd) 확인 완료
            base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
            key = config('API_KEY')
            api_url = f'{base_url}?key={key}&movieCd={movieCd}'

            response = requests.get(api_url)
            #print(response) # 200
            data = response.json()
            #pprint(data)

            movieInfoList = data.get('movieInfoResult').get('movieInfo')
            try:
                directors = movieInfoList.get('directors')[0]
            except:
                continue

            searchMovieInfoDicts = {}

            #pprint(movieInfoList)
            movieCd = movieInfoList.get('movieCd')
            movieNm = movieInfoList.get('movieNm')
            movieNmEn = movieInfoList.get('movieNmEn')
            movieNmOg = movieInfoList.get('movieNmOg')
            audits = movieInfoList.get('audits')[0]
            watchGradeNm = audits.get('watchGradeNm')

            
            openDt = movieInfoList.get('openDt')
            showTm = movieInfoList.get('showTm')
            genreNm = movieInfoList.get('genreNm')
            peopleNm = directors.get('peopleNm') # 중복인 actor peopleNm을 방지하기 위해 더 깊이 들어간다.
            companys = movieInfoList.get('companys')[0]
            companyNm = companys.get('companyNm')

            searchMovieInfoDicts['movieCd'] = movieCd
            searchMovieInfoDicts['movieNm'] = movieNm
            searchMovieInfoDicts['movieNmEn'] = movieNmEn
            searchMovieInfoDicts['movieNmOg'] = movieNmOg
            searchMovieInfoDicts['watchGradeNm'] = watchGradeNm
            searchMovieInfoDicts['openDt'] = openDt
            searchMovieInfoDicts['showTm'] = showTm
            searchMovieInfoDicts['genreNm'] = genreNm
            searchMovieInfoDicts['peopleNm'] = peopleNm
            searchMovieInfoDicts['companyNm'] = companyNm

            writer.writerow(searchMovieInfoDicts)