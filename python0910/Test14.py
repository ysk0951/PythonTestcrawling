'''
함수 function
#구조
def 함수명(param1, param2) :
    실행문들....
    return 값

함수명(인자1, 인자2)

#종류
    사용자 정의 함수
    내장 함수
    메서드 : 클래스 안에 있을때
    클래스밖에 있을때는 함수
    python 파일하나당 하나의 메인이라고 생각
'''

def showMsg():
    print("저는 함수 입니다.")

showMsg()

def getNum():
    print("return")
    return 10

num = getNum()
print(num)

def printName(name) :
    print("이름은 %s입니다." %name)
    
printName("라이츄")

def my_sum(num1,num2):
    result = num1+num2
    return result

result = my_sum(10,20)
print(result)

#
def my_mul(num1,num2):
    result = num1*num2
    return result
def my_div(num1,num2):
    result = num1/num2
    return result
def my_sub(num1,num2):
    result = num1-num2
    return result
result = my_sub(3,4)
print(result)
result = my_mul(3,4)
print(result)
result = my_div(3,4)
print(result)

