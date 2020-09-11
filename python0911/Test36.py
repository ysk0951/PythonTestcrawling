#트럼프 카드
'''
클래스변수 : 모든객체공유
인스턴스변수 : 각 객체만의 유일한 데이터 저장
지역변수 : 메서드 실행중 연산등을 위한 데이터를 잠시 저장

#메서드
    1. 인스턴스 메서드
        일반적인 클래스 정의할때 작성하는 메서드
        첫번째 매개변수는 반드시 self
    2. 생성자
    3. 클래스 메서드
    4. 스태틱 메서드
'''
class Card:
    #클래스
    width = 80
    height = 130
    def __init__(self,shape,number):
        #인스턴스
        self.shape = shape
        self.number = number
c1 = Card("spade",5)
c2 = Card("heart",7)

print(c1.shape)
print(c1.number)
print(c1.width)
print(c1.height)
print("="*30)

Card.width = 40
Card.height = 88
print(c1.shape)
print(c1.number)
print(c1.width)
print(c1.height)