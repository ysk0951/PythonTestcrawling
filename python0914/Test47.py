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

# print("프로그램 시작")
# while True:
#     try:
#         num = input("점수 : ")
#         int(num)
#         print(num)
#         break
#     except ValueError:
#         print("error")
#         break
# print("프로그램 종료")

# lst = [1,2,3]
# try :
#     idx = int(input("인덱스 번호 입력 : "))
#     print(lst[idx])
# except IndexError as e:
#     print("index Error =",end=" ")
#     print(e)

def func():
    num =int(input("1~5 사이 정수 입력 :"))
    print(num)

