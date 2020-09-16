'''
정규 표현식 파이썬 모듈 re
사용방법
1) 패턴 만들기
2) 패턴 이용하여 match(문자열),search(문자열)
            ,findall(문자열),finditer(문자열)로 활용
3) 위에서 받은 결과물을 group(),start(),end(),span()을 이용해서 리턴
'''
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>tes Title</title>
</head>
<body>
    <p id = "i" class="a">111</p>
    <p class="b">222</p>
    <p class="b">333</p>
    <a href="/test/test01">a tag</a>
    <b>b tag</b>
</body>
</html>
'''
import re
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')
# re.compile('정규표현식') : 패턴을 만들어줌
# find_all(태그명), find_all(class="값"), find_all(id='값')
# print(soup.find_all(class_=re.compile('a')))
# print(soup.find_all(id=re.compile('i')))
# print(soup.find_all(re.compile('t'))) #t가 포함된 태그
# print(soup.find_all(re.compile('^t'))) #t로 시작하는 태그
# print(soup.find_all(href=re.compile('/'))) #/가 들어간 하이퍼링크

str = "test fefwef f test1"
pattern = re.compile('test') #패턴 만들기
a = pattern.match(str) #패턴에 맞는 형태 추출
# print(a) # 첫번째 찾음
# print(a.group()) # 찾은 결과
# print(a.start()) # 찾은 단어 시작 인덱스번호
# print(a.end()) # 찾은 단어 끝 인덱스 +1

b = pattern.search(str)
# print(b)
# print(b.group())
# print(b.start())
# print(b.end())

# c = pattern.findall(str)
# print(c)
# for i in c:
#     print(i)
#
# d = pattern.finditer(str)
# for i in d :
#     print(i.group(),i.start(),i.end(),i.span())

str = """I am hungry. I like Pycharm.
Sample String for RE testa :
abcefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+.,!@#$%^&*()'"
12345 -99.8.3.14 .69394 5,000 +12 
"""
#[0-9]
pattern1 = re.compile('[0-9]+')
res = pattern1.findall(str)
# print(res)

#[a-z]
pattern2 = re.compile('[a-z]+')
res = pattern2.findall(str)
# print(res)

#[A-Z]
pattern3 = re.compile('[A-Z]+')
res = pattern3.findall(str)
# print(res)

#[a-zA-Z]
pattern4 = re.compile('[a-zA-Z]+')
res = pattern4.findall(str)
# print(res)

# \d 숫자
# mob = "전화번호 070-1111-2222"
# pattern5 = re.compile('[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
# pattern6 = re.compile('010-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
# pattern7 = re.compile('070-\d\d\d\d-\d\d\d\d')
# pattern7 = re.compile('070-\d{4}-\d\d\d\d')
# res5 = pattern5.findall(mob)
# res6 = pattern6.findall(mob)
# res7 = pattern7.findall(mob)
# print(res7)

# \w 문자 \d 숫자 {} 반복
pattern = re.compile('[^a-zA-Z0-9]+')
print(pattern.findall(str))

# . : 문자열의 자리표현
pattern1 = re.compile('t..t')
print(pattern1.findall(str))

# ? : t?est : test,est
# \w+ : 1개이상 있는것
# \w* : 뒤에 있어도 되고 없어도 되는
pattern1 = re.compile('t?est\w+')
print(pattern1.findall(str))

# 한글 범위
# [ㄱ-힣] : X
# [ㄱ-ㅎ]-[가-깋] : [가~힣]
# [0-9a-zA-Z가-힣] > 한글영어숫자 전부포함