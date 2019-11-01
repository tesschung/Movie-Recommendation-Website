import requests
from bs4 import BeautifulSoup as bs

url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'

response = requests.get(url)
print(response.text)
soup = bs.find_all('div')
print(soup)
# soup = BeautifulSoup(response, 'html.parser')