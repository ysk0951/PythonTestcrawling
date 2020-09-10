#군집자료형 : 문자열, 리스트, 튜플, 딕셔너리, 집합
'''
# 튜플 tuple
    리스트 : [] mutable
    튜플 : (,) immutable(수정안됨)
    튜플에 데이터가 한개일때는 소괄호로 묶어서 반드시 쉼표까지 기술
    데이터가 열개일 때, 괄호 생략 가능(쉼표로 구분)
'''
# t1 = () #literal 방식
# print(t1)
# print(type(t1))
#
# t2= tuple()
# print(t2)
# print(type(t2))

#한개의 요소만 튜플에 저장
#튜플에 하나만 넣어서 괄호를 치면 연산기호로 인식하므로,쉼표를 넣어줘야한다.
# t2 = (10)
# t2 = ("tuple")
# print(t2)
# print(type(t2))
#
# t3 = ("tuple",)
# print(t3)
# print(type(t3))
#
# 두개 이상일 경우 소괄호 생략 가능
# t3 = 1,2,3
# print(t3)
# print(type(t3))

# t4 = 1,2,"abc","Z"
#TypeError: 'tuple' object does not support item assignment
# t4[0] = 100
# print(t4)

#List : mutable
# t5 = (1,2,[3,4,5],6,7)
# t5[2][0] = 300
# print(t5)

#tuple unpacking
# tup = ("피카츄",10,"서울")
# name , age , city = tup
# print(name,age,city)

# a= 10
# b= 20
# a,b = b,a
# print(a, b)

# t1 = (1,2,3)
# t2 = ("a","b","c")
#tuple extention
# t3 = t1+t2
# print(t3)

#튜플 요소 할당
# t2 = t1*2
# print(t2)

# tup = (1,2,'a','b')
# print('a' in tup)
# print('abc' in tup)

# tupList = [("피카츄",30),("라이츄",70),("꼬북이",90)]
# for i,j in tupList:
#     print(i,"님의 점수는",j,"점입니다")
#
# tup = ("global",[1,2,3],(4,5,6))
# print(tup[1][1])
# print(tup[1][1:])
# print(tup[2][:2])
#
# sum(),len()
# t1 = (1,2,3,4,5)
# print(sum(t1))
# print(len(t1))
# print(min(t1))
# print(max(t1))

#index(값)
# print(t1.index(3))

# count() : 요소의 개수 구하기
# t1 = 1,1,1,2,2
# print(t1.count(1))
# print(t1.count(2))

#Q1 sum() 함수 구현
# def sum_(*num):
#     tot = 0
#     value = 0
#     for i in num:
#         tot +=i
#     print("total",tot)
#     return tot
#Q2 max() 함수 구현
# def max_(*num):
#     value = 0
#     max = 0
#     initialize = False
#     for i in num:
#         if not initialize:
#             max = i
#             initialize = True
#         if i >= max:
#             print(i,"가 기존의 최대값인 ",max,"보다 크거나 같습니다")
#             max = i
#     print("max",max)
#     return max
# max_(1,2,3,6)
#Q3 min() 함수 구현
# def min_(*num):
#     value = 0
#     min = 0
#     initialize = False
#     for i in num:
#         if not initialize:
#             min = i
#             initialize = True
#         if i <= min:
#             print(i,"가 기존의 최대값인 ",min,"보다 작거나 같습니다")
#             min = i
#     print("max",min)
#     return min
# min_(6,3,2,1)
#Q4 index() 함수 구현
#Q5 count() 함수 구현
#Q6 (심화) replace() 함수 구현