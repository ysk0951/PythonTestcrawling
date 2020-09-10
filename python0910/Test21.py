'''
def 함수명(*파라미터):
    실행문들...
'''
# sum 함수에 원하는 만큼 숫자를 보내면 모두 더한 총 합을 리턴해주는 함수
# * 는 tuple을 받거나 만든다고 생각하면 편함
def sum(*num):
    print(num)
    tot = 0
    for i in num:
        tot+=i
    return tot

result = sum(10,20,30,40)
print(result)

# 원하는 연산 기호와, 원하는 만큼의 정수들을 인자로 보내면 연산기호에 맞는 결과를 리턴해주는 함수
def calc(op,*num,msg="default"):
    if op == "sum":
        tot = 0
        for i in num:
            tot += int(i)
    elif op == "mul":
        tot = 1
        for i in num:
            tot *= int(i)
    print("msg :" ,msg)
    return tot

calc("sum",10,20,"30",msg="helle~SUM")
