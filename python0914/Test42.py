'''
파이썬 다중 상속 주의점
: 클래스/메서드 탐색 순서는 MRO(Method Resolution Order)를 따른다.
다중 상속시 우선순위는 왼>오 순서로 높다
동일한 이름의 메서드가 둘 이상의 부모에 존재하면,
왼쪽 부모 클래스의 메서드가 실행된다
mro f통해 순서 확인가능
최고조상은 object
'''
class A:
    pass
print(A.mro())

class B(A):
    pass
print(B.mro())
class C(A):
    pass
print(C.mro())
class D(B,C):
    pass
print(D.mro())

class E(C,B):
    pass
print(E.mro())

class F(D,E):
    pass

print(F.mro())
