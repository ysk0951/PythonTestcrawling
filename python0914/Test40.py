'''
# 클래스 상속
    class A: #부모
        변수 + 메서드
    class B(A,B,C): #자식
        변수 메서드

# 다중상속 허용
# 메서드 오버라이딩
    : 상속 관계에서 성립
'''

class Student1:
    def python(self):
        print("신기한 파이썬")
class Student2:
    def java(self):
        print("재밌는 java")
class Student3:
    def c(self):
        print("재미없는 c")
class Pika(Student1,Student2,Student3):
    pass

pika = Pika()
pika.python()
pika.java()
pika.c()