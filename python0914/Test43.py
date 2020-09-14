class A:
    def hello(self):
        print("hello AAAA")
class B(A):
    def hello(self):
        print("hello BBBB")
class C(A):
    def hello(self):
        print("hello CCCC")

class D(B,C): #D > B > C > A
    def hello(self):
        # 한단계 위
        super(D, self).hello()
        super(C, self).hello()
        super(B, self).hello()
        pass
x = D()
x.hello()
