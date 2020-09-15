'''
기상청
서울경기도
http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109
전국
http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
강원도
http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=105

stnId 파라미터 값 : 전국 100, 서울경기 109, 강원 105
'''
import urllib.request as request
import urllib.parse
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {'stnId' : '108'}
param = urllib.parse.urlencode(values)

# url 완성
url = API +"?"+param
print(url)

# 정보요청 다운받기
page = request.urlopen(url)
data = page.read()
text = data.decode("utf-8")
print(text)