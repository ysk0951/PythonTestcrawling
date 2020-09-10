'''
def 함수명(*파라미터):
    실행문들...
'''
#sum 함수에 원하는 만큼 숫자를 보내면 모두 더한 총 합을 리턴해주는 함수
# * 는 tuple을 받거나 만든다고 생각하면 편함
def sum(*num):
    tot = 0
    for i in num:
        tot+=i
    return tot

result = sum(10,20,30,40)
print(result)
