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

html = """<p>test</p>"""
print(html)
print(type(html))
print("="*40)
soup = BeautifulSoup(html,"lxml")
print(soup)
print(type(soup))
print("="*40)
soup = BeautifulSoup(html,"html.parser")
print(soup)
print(type(soup))

