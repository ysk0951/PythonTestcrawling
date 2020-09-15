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
#
# html = '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title class="t a b" id="tid">test Title</title>
# </head>
# <body>
#     <p>1111</p>
#     <p>2222</p>
#     <p>3333</p>
# </body>
# </html>'''
#parsing
# soup = BeautifulSoup(html,'lxml')
# print(soup)
# print(type(soup))
# print("="*40)

#1. 간단한 태그 접근
# title = soup.title
# p = soup.body
# print(title,                        # 태그전체
#       "\ntype=",type(title),        # 태그의 타입
#       "\ntext=",title.text,         # 태그의 내부텍스트와 하위태그포함
#       "\nStringType=",title.string) # 태그의 내부텍스트중의 값
# print(p)

#2. 태그의 속성접근
# soup = BeautifulSoup(html,'lxml')
# t_tag = soup.title
# print(t_tag.attrs) # class >> list
# print(t_tag['class']) # dictionary에서 key로 value꺼내기 - 없으면  Error
# print(t_tag.get('class')) # dictionary에서 key로 value꺼내기 - 없을시 None

# html = '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title class="t a b" id="tid">test Title</title>
# </head>
# <body>
#     <p>
#           <span>1111</<span>
#           <span>2222</<span>
#     </p>
# </body>
# </html>'''
# soup = BeautifulSoup(html,'lxml')
# p_tag = soup.p
#
# text_data = p_tag.text
# string_data = p_tag.string
#
# print("text : ",text_data,type(text_data)) # 자식포함
# print("string : ",string_data,type(string_data)) # 바로밑에만 읽기
#-----------------------------------------------------------------------------------
# p_tag_c = soup.p.contents
# print("tag_c",p_tag_c)
#
# p_tag_ch = soup.p.children
# print("tag_ch",p_tag_ch)
# for child in p_tag_ch:
#       print(child)

#부모태그 접근
# span_tag = soup.span
# print(span_tag)
# print(span_tag.parent)
# print("="*50)
# parents = span_tag.parents
# for p in parents:
#       print(p)

# 형제 태그 접근 : next_sibling,previous_sibling
# html = '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title class="t a b" id="tid">test Title</title>
# </head>
# <body>
#     <p>
#           <span>1111</<span>
#           <span>2222</<span>
#     </p>
# </body>
# </html>'''
# soup = BeautifulSoup(html,'lxml')
# span_tag = soup.span
# n = span_tag.next_sibling
# p = span_tag.previous_sibling
# print(n)
# print(p)

# 이전 요소, 다음 요소 : next_element(s), previous_element(s)
# html = """<head>
#     <title>test</title>
# </head>
# <body>
#     <p>
#         <a>test1
#             <span>123</span>
#             <span>456</span>
#         </a>
#         <b>test2</b>
#         <c>test3</c>
#     </p>
# </body>
# </html>
# """
# soup = BeautifulSoup(html,"lxml")
# print(soup)
# a_tag = soup.a
# print(a_tag)
# s = a_tag.next_sibling
# print(type(s))
# for ss in s:
#       print(ss)
# print("===========")
# e = a_tag.next_elements
# print(type(e))
# for ee in s:
#       print(ee)

'''원하는 요소 정확히 접근하기'''
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title class="t a b" id="tid">test Title</title>
</head>
<body>
    <p class = 'a'>1111</p>
    <p id="a">2222</p>
    <p class = 'b'>3333</p>
</body>
</html>'''
soup = BeautifulSoup(html,'lxml')
# print(soup.find_all('p'))     #태그명으로 가져오기
# print(soup.find_all(id='a'))  #id로 가져오기
# print(soup.find_all(id=True)) #속성존재여부로 가져오기
# print(soup.find_all(id=False))
# print(soup.find_all('p',id='a'))
# print(soup.find_all('p',class_='a'))#태그, class 속성 두개 지정해서 찾기
# print(soup.find_all('p',text='1111'))#text로 찾기
# print(soup.find_all('p',limit=4))#검색양 제한하기
# print(soup.find_all())#모든태그 가져오기
# print(soup.find_all(['title','p']))#태그 여러개
# 여러번 거르기
# body = soup.find_all('body')
# print(body)
# ps = body[0].find_all('p')
# print(ps)

# find()
# print(soup.find('body').find('p',class_='b'))
# select()
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test Title</title>
</head>
<body>
    <p class = 'a' id='i'>1111</p>
    <p class ='b'>2222</p>
    <p class ='b'>3333</p>
    <a href="/test/test01">a tag</a>
    <b> b tag </b>
</body>
</html>'''
soup = BeautifulSoup(html,'lxml')
print(soup.select('p'))
print(soup.select('.b'))
print(soup.select("p#i"))


