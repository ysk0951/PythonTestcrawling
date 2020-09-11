'''
class : 변수+함수

구조:
    # 클래스 정의
    class 클래스명:
        변수...
        메서드...

    #객체 생성
    변수명 = 클래스명()
'''
class Person:
    name = ""
    age = 0

#객체 생성
p1 = Person()
print(p1)

'''
#필드
    #1. 클래스 변수
        생성위치 : 메서드 밖, 클래스 안(static없음)
        * 단, 객체명으로 클래스변수의 값을 변경하게 되면, 인스턴스 변수로 새로 생성된다.
        이를 메모리 후위선점방식이라고 부른다.
    #2. 인스턴스 변수
        생성위치: 메서드 안 self.변수명
        사용법 : 객체명.변수명
    #3. 지역변수
        메서드 안에서 생성및 소멸

'''

class Starbucks :
    shape = ""

s1 = Starbucks() #1호점
s2 = Starbucks() #2호점
print(s1.shape)
print(s2.shape)
print("="*30)
Starbucks.shape="Star"
print(Starbucks.shape)
print(s1.shape)
print(s2.shape)
print("="*30)
s1.shape="diamond"
print(Starbucks.shape)
print(s1.shape)
print(s2.shape)
print("="*30)