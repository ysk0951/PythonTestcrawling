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
t2 = (10)
t2 = ("tuple")
print(t2)
print(type(t2))

t3 = ("tuple",)
print(t3)
print(type(t3))

# 두개 이상일 경우 소괄호 생략 가능
t3 = 1,2,3
print(t3)
print(type(t3))