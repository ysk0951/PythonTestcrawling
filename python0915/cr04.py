"""
BeautifulSoup
-parsingModule

# 파서의 종류
# lxml(HTML parser)
    BeautifulSoup(html,'lxml')
    c로 구성, 속도빠름, lib 추가
# lxml(XML parser)
    BeautifulSoup(html,'lxml-xml')
    유일하게 지원되는 xml parser
# Html5lib
    BeautifulSoup(html,'html5lib')
    느림, lib 추가
# Html.parser
    BeautifulSoup(html,'html.parser')
    보통 속도, lib추가 X
"""
from bs4 import BeautifulSoup

# html = """<p>test</p>"""
# print(html)
# print(type(html))
# print("="*40)
# soup = BeautifulSoup(html,"lxml")
# print(soup)
# print(type(soup))
# print("="*40)
# soup = BeautifulSoup(html,"html.parser")
# print(soup)
# print(type(soup))

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title class="t" id="tid">test Title</title>
</head>
<body>
    <p>1111</p>
    <p>2222</p>
    <p>3333</p>
</body>
</html>'''
#parsing
soup = BeautifulSoup(html,'lxml')
print(soup)
print(type(soup))
print("="*40)

#1. 간단한 태그 접근
title = soup.title
p = soup.body
print(title,                        # 태그전체
      "\ntype=",type(title),        # 태그의 타입
      "\ntext=",title.text,         # 태그의 내부텍스트와 하위태그포함
      "\nStringType=",title.string) # 태그의 내부텍스트중의 값
print(p)

#2. 태그의 속성접근
soup = BeautifulSoup(html,'lxml')
t_tag = soup.title
print(t_tag.attrs) # class >> list
print(t_tag['class']) # dictionary에서 key로 value꺼내기 - 없으면  Error
print(t_tag.get('class')) # dictionary에서 key로 value꺼내기 - 없을시 None
