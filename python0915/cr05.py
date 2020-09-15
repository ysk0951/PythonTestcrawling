import  requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/read.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230&oid=082&aid=0001028994"
res = requests.get(url)
soup = BeautifulSoup(res.content,'lxml')
# print(soup.prettify())
#print(soup.find('title').text)
#print(soup.select('.photo'))
#기사제목
headLine = soup.find(id='articleTitle').text
print(headLine)
#기사본문
content = soup.find(id='articleBodyContents').text
print(content)

contents = soup.find(id='articleBodyContents').text.strip()
print(contents)