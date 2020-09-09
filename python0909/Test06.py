'''
num1 = 10
num2 = 3
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)#실수
print(num1//num2) #몫
print(num1%num2) #나머지
'''
'''
# 문제 1 분자 분모를 하나씩 입력받고 몫과 나머지 출력
x = int(input("분자 입력"))
y = int(input("분모 입력"))
result1 = x//y
result2 = x%y
print("몫은 {}이고 나머지는 {}입니다" .format(result1,result2))

# 문제2 1000초를 ?분 ?초로 출력하세요
min = 1000//60
sec = 1000%60
print("1000초는 {}분 {}초 입니다" .format(min,sec))

#복합대입연산
num1 = 10
num2 = 20
num1 +=10
num1 -=5
num1 -=num2

#논리 연산자
#&&  >>  and
#||  >>  or
#! >> not 
'''