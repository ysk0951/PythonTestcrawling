'''
연산자
    산술 연산자 : + - * / %
    대입 연산자 : =
    복합대입 연산자 : += -= *= /= %=
    비교 연산자 : > <= < <= == !=
    논리 연산자 : True / False
    멤버 연산자 : in / not in
    식별 연산자 : is / is not
'''
#import
import datetime
date = datetime.date.today();
print(type(date))
date = str(date)
print(date)
print(date[0:4]+"년"+date[5:7]+"월"+date[8:]+"일")

#문자열 함수
str = "Global IT"
str = str.replace("IT","institute")
print(str)