'''
변수의 scope
1. global
    선언위치 : 함수밖
    유효범위 : 프로그램이 종료될때까지
            함수안에서 사용할시 참조형으로만 사용가능(함수 내에서 변경불가)
    #함수안에서 값을 변경하는 방법
    #1. 리턴값 이용
    #2. global 키워드 이용하기
2. local
    선언위치 : 함수안
    유효범위 : 함수안에서만, 함수가 종료될때 소멸
'''
# def func(num) :
#     num = num + 1
#     print("지역",num)
#
# num = 20
# func(num)
# print("전역",num)
#

num2 = 10
def func2(num):
    num = num+10
    return num
num2 = func2(num2)
print("num2",num2)

#Global keyword
num3 = 10
def func3():
    global num3
    num3 +=10
func3()
print(num3)