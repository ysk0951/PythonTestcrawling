'''
제어문
    1) 조건문 : if
    2) 반복문 : while for
    3) 보조제어문 : break, continue

1) 조건문 if
if 조건문:
    실행문장
elif 조건문:
    실행문장
elif 조건문:
    실행문장
else
    실행문장
------------------

score = 50
if score >=60:
    print("합격")
else:
    print("불합격")
'''

# 문제1 : 점수를 하나 입력받고 그 수가 양수인지 음수인지 출력
num1 = int(input("문제1 점수"))
if num1>=0:
    print("양수")
else:
    print("음수")
# 문제2 : 정수를 하나 입력받고 그 수가 짝수인지 홀수인지 출력
num2 = int(input("문제2 점수"))
if num2%2==0:
    print("짝수")
else:
    print("홀수")
# 문제3 : id와 pw를 하나씩 입력받고 dbid와 dbpw가 일치하는지 출력
dbid = "python"
dbpw = "1234"
str_id=input("문제3 id")
str_pw=input("문제3 pw")
if str_id==dbid:
    print("id일치")
elif str_pw==dbpw:
    print("pw일치")
else:
    print("불일치")
