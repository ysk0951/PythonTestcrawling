'''
## requests
    파이썬에서 http요청을 보낼때 사용되는 모듈
    requests로 http요청을 하면 응답에 관련된 정보들을 함께 응답객체로 반환해줌
    라이브러리 추가 설치 필요함
## BeautifulSoup
    HTML의 태그를 파싱해서 필요한 데이터만 추출하는 함수를 제공하는 라이브러리

    urllib + bs
    request + bs
'''
import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "http://www.naver.com"
res = requests.get(url)
# print(res.status_code)
# print(list(res.cookies))
# pprint(res.headers)

#html코드보기
#print(res.text)
# print(res.content)
# print(res.encoding)

#.get()
#쿼리스트링 만들어 요청
res = requests.get(url,params={"key1":"value1","key2":"value2"})
# print(res.url)

#.post()
# post는 body에 인자 셋팅
res = requests.post(url,data={"key1":"value1","key2":"value2"})
# print(res.url)
# print(dict(res.headers))

import json
res = requests.post(url,data=json.dumps({"key1":"value1","key2":"value2"}))
# print(res.headers)

'''
request 예외처리
HTTPError
connectionError
ProxyError
SSLError
Timeout
ConnectTimeout
URLRequired
TooManyRedirect
MissingSchema
InvalidURL
ContentDecodingError
RetryError

try:
except request.exeptions.HttpError :

'''
import requests
try:
    url = "naver.com/test"
    res = requests.get(url)
    print(res.url)
except requests.exceptions.HTTPError:
    print("Http Error")
except requests.exceptions.Timeout:
    print("timeout Error")
except requests.exceptions.MissingSchema:
    print("Missint schema Error")