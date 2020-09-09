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

#문자열 나누기 : split()
a,b,c,d,e = "1 2 3 4 5".split();#공백을 기준으로 나눔
print(a)

str1 = "Global:it"
a,b = str1.split(":")
print(a)
print(b)

#문자열 길이 : len()
str="wetwet234t13dsadeefaefwegwgwerewrafdsf"
print(len(str))

#문자의 개수 : count()
print(str.count("s"))

#위치 알려주기
# find 해당문자없으면 -1
# index 해당문자없으면 error
str2 = "global it"
print(str2.find("o"))
print(str2.index("o"))

#소문자로 바꾸기 : lower()
str = "AltoDs"
str = str.lower()
print(str)
str = str.upper()
print(str)

#공백지우기 : strip(), lstrip(), rstrip()
str = "        python        "
print(str)
print(str.rstrip())
print(str.lstrip())
print(str.strip())