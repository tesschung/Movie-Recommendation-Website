# Project_08: 

1. 목표
API 요청에 대한 이해
RESTful API 서버 구축
API 문서화

2. 준비 사항

3. (필수) Python Web Framework
  Django 2.2.x
  Python 3.7.x

4. 요구 사항

5. 데이터베이스 설계
  db.sqlite3 에서 테이블 간의 관계는 아래와 같습니다.
  필드명 자료형 설명
  id Interger Primary Key
  title String 영화명
  audience Integer 누적 관객수
  poster_url String 포스터 이미지 URL
  description Text 영화 소개
  genre_id Integer Genre의 Primary Key(id 값)
  movies_movies
  필드명 자료형 설명
  id Interger Primary Key
  name String 장르 구분
  movies_genres
  movies_reviews
  필드명 자료형 설명
  id Integer Primary Key
  content String 한줄평(평가 내용)
  score Integer 평점
  movie_id Integer Movie의 Primary Key(id 값)
  user_id Integer User의 Primary Key(id 값)
6. Seed Data 반영
7. 주어진 movie.json 과 genre.json 을 movies/fixtures/ 디렉토리로 옮깁니다.
8. 아래의 명령어를 통해 반영합니다.
9. admin.py 에 Genre 와 Movie 클래스를 등록한 후, /admin 을 통해 실제로 데이터베이스에 반영
  되었는지 확인해봅시다.
10. movies API
  아래와 같은 API 요청을 보낼 수 있는 서버를 구축해야 합니다.
  허용된 HTTP 요청을 제외하고는 모두 405 Method Not Allowed를 응답합니다.
11. GET /api/v1/genres/
   장르의 목록을 요청 받아서 다음과 같은 결과를 응답합니다.
   $ python manage.py loaddata genre.json
   Installed 11 object(s) from 1 fixture(s)
   $ python manage.py loaddata movie.json
   Installed 10 object(s) from 1 fixture(s)