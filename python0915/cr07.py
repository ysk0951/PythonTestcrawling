#네이버 뉴스기사
from typing import List, Any

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

# soup = BeautifulSoup(res.content,"lxml")
# dataByday = soup.select(".title")
# for i in dataByday:
#     day = i.attrs['href'][-3:]
#     print(i.attrs['href'][-3:])
# print(dataByday)



# for ii in i:
#     print(ii)
# print(i+1,":",data[i].text.strip())

#네이버 미세먼지
html = requests.get('https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(html.content,"lxml")
# print(soup.prettify())
# data= soup.find('dd',class_='lv1')
# print(data.text)

data = soup.find('dl',class_='indicator')
print(data.prettify())
dt = data.find_all('dt')

for d in dt:
    print(d.text)
    # dt_list.append(d.text)

find_dust= []
span = data.find_all('span',{'class':'num'})
for s in span:
    print(s.text)

dd= data.find_all('dd',class_='lv1')
for d in dd:
    print(d.text)
dt_list=[]
find_dust= []
find_dust_status = []
span = data.find_all('span',{'class':'num'})
for s in span:
    find_dust.append(s.text)
    find_dust_status.append(s.next_sibling)

for i in range(3):
    print(dt_list[i],"=",find_dust[i],find_dust_status[i])

with open('findDust.txt','w',encoding="utf-8") as file:
    for i in range(3):
        str = dt_list[i]+"="+find_dust(i)+find_dust_status(i)+"\n"
        file.write(str)


