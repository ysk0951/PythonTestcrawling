# 정보 은닉
class MyClass:
    # 외부에서 볼수 없다
    __num1 = 1
    def printAttr(self):
        print(MyClass.__num1)

m = MyClass()
m.printAttr()
