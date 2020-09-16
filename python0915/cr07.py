#네이버 뉴스기사

import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=259"
res = requests.get(url)
soup = BeautifulSoup(res.content,'lxml')
data = soup.select('ul.type06_headline>li>dl>dt:nth-child(2)>a')
# # print(data)
# for i in data :
#     print(i.text.strip())

#네이버 영화 평점
#네이버 웹툰 요일별 리스트 + 썸네일(저장 > urlretrieve)
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
# soup = BeautifulSoup(res.content,'lxml')
# data = soup.select(".title")
# day = soup.select(".col_inner")
# for i in day :
#     # soup.select()
#     print(i.text.strip())
#     print("=" * 30)

# for i in data :
#     print(i.text.strip())

soup = BeautifulSoup(res.content,"lxml")
dataByday = soup.select(".title")
for i in dataByday:
    day = i.attrs['href'][-3:]
    print(i.attrs['href'][-3:])
# print(dataByday)



# for ii in i:
#     print(ii)
# print(i+1,":",data[i].text.strip())


#네이버 미세먼지
html = requests.get('https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8')
print(html.text)