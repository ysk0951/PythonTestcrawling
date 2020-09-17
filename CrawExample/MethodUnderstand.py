class Payment:
    count = 0
    discount = 0.3

    # 생성자
    def __init__(self, price, number):
        self.price = price
        self.number = number
        Payment.count += 1

    # 인스턴스 메서드
    def calculator(self):
        self.pay = self.price * self.number
        self.dc_pay = self.pay - (self.pay * Payment.discount)

    def display(self):
        print(Payment.count, "번째 제품입니다.")
        print("정가 : ", self.price)
        print("수량 : ", self.number)
        print("가격 : ", self.pay)
        print("할인가격 : ", self.dc_pay)

    @staticmethod
    def message():
        print("할인중입니다")

    @classmethod
    def update(cls, val):
        while (val >= 1) or (val <= 0):
            val = float(input("할인율을 다시 입력하세요"))
        cls.discount = val


# --------------------------------------------------------------
p1 = Payment(1000, 5)
p1.calculator()
p1.display()

p2 = Payment(5000, 3)
p2.calculator()
p2.display()
p2.update(5)

'''
파이썬은 생성된 인스턴스에서 클래스함수에 접근할수있다는것이 특징이다.
그것때문에 cls와 self가 존재한다고 생각하면된다.
'''
