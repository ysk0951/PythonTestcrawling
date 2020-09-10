# 문제1. 계산기
"""
사칙연산을 모두 수행하여 결과를 보여주는 프로그램만들기
단, 사용자에게 종료여부를 물어서,
y를 입력하면 프로그램 종료, n을 입력하면 계속 진행~~~

콘솔 출력예)
정수1 입력:  10
정수2 입력:  20
덧셈: 30
뺄셈: -10
곱셈: 200
나눗셈: 0.5

종료하시겠습니까?(y/n) : n

정수1 입력:
정수2 입력:
덧셈:
뺄셈:
곱셈:
나눗셈:

종료하시겠습니까?(y/n) : y

프로그램종료!!
"""
#1. 통으로 전역에 만들어주시고
# while True:
#     num1 = int(input("정수1 입력 :"))
#     num2 = int(input("정수2 입력 :"))
#     print("덧셈:",num1+num2)
#     print("뺄셈:",num1-num2)
#     print("곱셈:",num1*num2)
#     print("나눗셈:",num1/num2)
#     option = input("종료하시겠습니까?(y/n)")
#     if option == "y" :
#         break
#2. 함수로 분리시켜보기.(사칙연산 출력하는것만)
# def sum(num1,num2):
#     result = num1+num2
#     return result
# def sub(num1,num2):
#     result = num1-num2
#     return result
# def mul(num1,num2):
#     result = num1*num2
#     return result
# def div(num1,num2):
#     result = num1/num2
#     return result
# while True:
#     num1 = int(input("정수1 입력 :"))
#     num2 = int(input("정수2 입력 :"))
#     print("덧셈:",sum(num1,num2))
#     print("뺄셈:",sub(num1,num2))
#     print("곱셈:",mul(num1,num2))
#     print("나눗셈:",div(num1,num2))
#     option = input("종료하시겠습니까?(y/n)")
#     if option == "y" :
#         break
#3. 전체를 함수로 넣어보기(옵션)
# def cal(num1,num2):
#     while True:
#         num1 = int(input("정수1 입력 :"))
#         num2 = int(input("정수2 입력 :"))
#         print("덧셈:", num1+num2)
#         print("뺄셈:", num1-num2)
#         print("곱셈:", num1*num2)
#         print("나눗셈:",num1/num2)
#         option = input("종료하시겠습니까?(y/n)")
#         if option == "y":
#             break

