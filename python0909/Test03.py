'''
#입력함수 : input()
    콘솔을 통해 사용자로 부터 입력을 받는 함수
    모두 문자열로 받아옴

#형변환
    문자 >> 정수/실수
        int(값)/float(값)
    정수,실수 >> 문자
        str(값)
'''

#age = input("나이을 입력하세요.")
#age = int(age)
#print(age+10)

#문자열 str
#"문자열" '문자열' """여러문자열""" '''여러문자열'''
print("""hello
python
hahahah""")

#문자열 연산
a = "pyton"
b = "더하기"
c = a+b
print(c)
print(a+b)
print(a,b)

#2. 문자열 반복하기 : *
print(a*10)
d = a*10
print(d)

#
#person1 = int(input("입력1"))
#person2 = int(input("입력2"))
#person3 = int(input("입력3"))
#result = (person1+person2+person3)/3
#print("결과는 %.1f입니다" %result)

#문자열indexing
str = "hello"
print(str[0])
a = "Global"
print(a[0])

