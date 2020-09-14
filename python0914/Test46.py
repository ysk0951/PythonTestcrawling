'''
#특수메서드
1)__init__(self) 생성자
2)__del__(self) 소멸자
    : del 명령어로 객체를 삭제하겠다 명령하면, 해당 객체의
    레퍼런스 카운트가 -1이 되고 레퍼런스 카운트가 0 이 될때
    소멸자가 자동 호출됨.
    실행이 종료되면 실행될 수 있다.

'''
class Character:
    a = 10
    def __init__(self):
        print("생성자 호출")
    def show(self):
        print("show!!!!")
    def __call__(self, *args, **kwargs):
        print("call 메서드 호출")
    def __getitem__(self, item):
        if item == 'a':
            return self.a
        elif item == 'b':
            return self.b
    def __del__(self):
        print("소멸자 호출")
# c1.show()
# c2.show()
# c3.show()
# c1()
# print(c1["a"]) #10

if __name__ == '__main__':
    c1 = Character()
    c2 = Character()
    c3 = Character()
    print(c1["a"]) #10
