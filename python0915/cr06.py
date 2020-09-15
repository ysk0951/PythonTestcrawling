#네이버 실시간 검색어 크롤링
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Chrome : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s&where=main"
res = requests.get(url, headers = headers)

soup = BeautifulSoup(res.content,"lxml")
data = soup.find_all('span',class_='item_title')
for i in range(len(data)):
    print(i+1,":",data[i].text)
