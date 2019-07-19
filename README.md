[TOC]

## Movie Crawler

**Crawling Movie Data using ''영화진흥위원회 오픈 API'' with Python**

`python 3.7`



#### Overview

50주간의 <주간 박스오피스 TOP10> 수집하기



#### Requirements

module `request`

API `영화진흥위원회 오픈 API`



#### Module

`requests` `pprint` `datetime` `decouple` `csv`



#### Goal

1. [영화진흥위원회 오픈 API](http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do?serviceId=searchDailyBoxOffice)(주간/주말 박스오피스 데이터) 

**최근 50주간 데이터 중에 주간 박스오피스 TOP10데이터**를 수집합니다. 해당 데이터는 향후 영화평점서비스에서 기본으로 제공되는 영화 목록으로 사용될 예정입니다.

*요청 조건*

주간(월~일)까지 기간의 데이터를 조회

조회 기간은 총 50주이며

기준일(마지막 일자)은 2019년 7월 13일입니다.

다양성 영화/상업 영화를 모두 포함하여야 합니다.

한국/외국 영화를 모두 포함하여야 합니다.

모든 상영지역을 포함하여야 합니다.

*결과*

| 응답필드 | 문자열 | 설명                          |
| -------- | ------ | ----------------------------- |
| movieCd  | 문자열 | 영화의 대표코드를 출력합니다. |
| audiCnt  | 문자열 | 해당일의 관객수를 출력합니다. |
| audiAcc  | 문자열 | 누적관객수를 출력합니다.      |

- [ ] 영화 대표코드 , movieCd

- [ ] 영화명 , movieNm

- [ ] 해당일 누적관객수 audiCnt 를 기록합니다.

- [ ] 해당일 누적관객수 는 **중복시** **최신** 정보를 반영하여야 합니다.
  
  예) 영화 엄복동이 20190713 기준 50,000명이고, 20190106 기준 5,000명이면 50,000명이 저장되어야 합니다.
  해당 결과를 boxoffice.csv 에 저장합니다.



2. 영화진흥위원회 오픈 API(영화 상세정보) 


- 요청 parameter : 3번항의 요청 인터페이스 정보를 참조하여 GET 방식으로 호출

  위에서 수집한 **영화 대표코드**를 활용하여 상세 정보를 수집합니다. 

  해당 데이터는 향후 영화평점서비스에서 영화 정보로 활용될 것입니다.

  *결과*

  영화별로 다음과 같은 내용을 저장합니다.
  
  영화 대표코드 , movieCd

  영화명(국문) , movieNm

  영화명(영문) , movieNmEn

  영화명(원문) , movieNmOg

  관람등급 , watchGradeNm

  개봉연도 , openDt

  상영시간 , showTm

   장르 , genreNm

  감독명 peopleNm
  해당 결과를 **movie.csv**에 저장합니다.
  
(선택) 배우 정보, 
  
-배우 actors
  
-배우명 peopleNm
  
-배역명 cast
  
배급사 정보
  
-영화사명 companyNm
  
   등을 추가적으로 수집할 수 있습니다.
  
  

3. 영화진흥위원회 오픈 API(영화인 정보) 


  위에서 수집한 영화 감독정보를 활용하여 상세 정보를 수집합니다. 

  해당 데이터는 향후 영화평점서비스에서 감독 정보로 활용될 것입니다.

  요청 조건  **영화인명**  으로 조회합니다.



  *결과*

  영화인별로 다음과 같은 내용을 저장합니다.

  영화인 코드 ,peopleCd

   영화인명 , peopleNm

  분야 , repRoleNm

  필모리스트 filmoNames
  해당 결과를 director.csv에 저장합니다.
  단, **만약 검색 결과가 없으면 저장할 필요 없습니다.**



#### Developement Method

1. http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do

   회원 가입 후 키를 발급 받으세요.

   발급키

2. 발급받은 키로 이제부터 다음과 같은 작업을 하겠습니다.

   key points:

   Json (Rest 방식)

   중요한 키값은 환경변수로 처리 .env

   파일로 저장 .csv

#### Start

이를 위해서 다음과 같은 작업을 시작합니다.

OPEN API

먼저 **주간/주말 박스오피스**를 확인합니다.

![1563498916413](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563498916413.png)

우리가 원하는 값은 다음과 같이 진행됩니다.


요청 조건

- [x] **주간**(월~일)까지 기간의 데이터를 조회합니다. weekGb=0

  

- [x] 조회 기간은 최근 50주간 데이터인 총 50주이며, datetime

- [x] 기준일(마지막 일자)은 2019년 7월 13일입니다.

  (요청할 url의 부분입니다.)



- [x] 주간 박스오피스 TOP10데이터인데, 그 데이터들은
- [x] 다양성 영화/상업 영화를 모두 포함하여야 합니다.
- [x] 한국/외국 영화를 모두 포함하여야 합니다.
- [x] 모든 상영지역을 포함하여야 합니다.

위와같이 Json으로 parsing한 데이터에서 아래의 정보를 찾아올것 입니다.

결과 수집된 데이터에서 아래 정보를 기록합니다.

- [x] 영화 대표코드 , movieCd

- [x]  영화명 , movieNm

- [x]  해당일 누적관객수 audiCnt : 해당일 누적관객수 는 **중복시** **최신** 정보를 반영
  예) 영화 엄복동이 20190713 기준 50,000명이고, 20190106 기준 5,000명이면 50,000명이 저장되어야 합니다.

  

끝으로, 해당 결과를 boxoffice.csv 에 저장합니다.

```python
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
    
            movieCd = weeklyBoxOfficeList.get('movieCd')
            movieNm = weeklyBoxOfficeList.get('movieNm') 
            audiCnt = weeklyBoxOfficeList.get('audiCnt')

            if movieCd not in weeklyBoxOfficeDicts:
                weeklyBoxOfficeDicts['movieCd'] = movieCd
                weeklyBoxOfficeDicts['movieNm'] = movieNm
                weeklyBoxOfficeDicts['audiCnt'] = audiCnt

             # Dictionary를 순회하며 key값에 맞는 value를 한줄씩 작성한다.
                writer.writerow(weeklyBoxOfficeDicts)
```



그리고 다음으로 **영화 상세정보**를 가져옵니다.

2. 영화진흥위원회 오픈 API(영화 상세정보) - 02.py 혹은 02.ipynb

   REST 방식

- 기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml (또는 .json)
- 요청 parameter : 3번항의 요청 인터페이스 정보를 참조하여 GET 방식으로 호출

  위에서 수집한 영화 **대표코드**를 활용하여 상세 정보를 수집합니다. 

  해당 데이터는 향후 영화평점서비스에서 영화 정보로 활용될 것입니다.

  

 *결과*
    영화별로 다음과 같은 내용을 저장합니다.

- [x] 영화 대표코드 , movieCd

- [x] 영화명(국문) , movieNm

- [x] 영화명(영문) , movieNmEn

- [x] 영화명(원문) , movieNmOg

- [x] 관람등급 , watchGradeNm

- [x] 개봉연도 , openDt

- [x] 상영시간 , showTm

- [x] 장르 , genreNm

- [x]   감독명 peopleNm
    해당 결과를 movie.csv에 저장합니다.

    
    
    (선택) 배우 정보, 
    
- [ ] -배우 actors

- [ ] -배우명 peopleNm

- [ ] -배역명 cast
  배급사 정보

- [x]   -영화사명 companyNm

   등을 추가적으로 수집할 수 있습니다.

![1563509845306](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563509845306.png)



그후 최종적으로 **영화인 정보**를 가져옵니다.

3. 영화진흥위원회 오픈 API(영화인 정보) - 03.py 혹은 03.ipynb

   REST 방식

- 기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.xml (또는 .json)
- 요청 parameter : 3번항의 요청 인터페이스 정보를 참조하여 GET 방식으로 호출

위에서 수집한 영화 감독정보를 활용하여 상세 정보를 수집합니다. 

해당 데이터는 향후 영화평점서비스에서 **감독 정보**로 활용될 것입니다.

여기서 문제가 발생합니다.

위 감독정보를 위한 영화인명은 **영화인목록** API에 들어가서 값을 찾을 수 있기때문에 영화인명을 위한 크롤링을 시작해야 합니다.

이후에 요청 조건인 영화인 코드 peopleCd로 조회합니다.

peopleCd로 접근하여 동명이인에 대한 정보를 살리기 위한 csv를 작성하게 되는 것입니다.



  *결과*

  영화인별로 다음과 같은 내용을 저장합니다.

- [x] 영화인 코드 ,peopleCd

- [x] 영화인명 , peopleNm

- [x] 분야 , repRoleNm

- [x] 필모리스트 filmoNames
  해당 결과를 director.csv에 저장합니다.
  단, **만약 검색 결과가 없으면 저장할 필요 없습니다.**

  

**그럼 크롤링 끝!**