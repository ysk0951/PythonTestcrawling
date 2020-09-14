'''
예외처리

IOError
IndexError
ImportError
ValueError
ZerodivsionError

try
    code
except error:
    예외 처리 code

'''
print("프로그램 시작")
while True:
    num = input("점수 : ")
    int(num)
    print(num)
    break
print("프로그램 종료")