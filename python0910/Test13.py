'''
for i in range(숫자):
    반복해서 실행할 명령문들....
range(stop) : 0 ~ stop 이전까지 1씩증가
range(start,stop) : start ~ stop 이전까지 1씩증가
range(start,stop,step) : start ~ stop 이전까지 step씩증가
'''
# for i in range(10):
#     print(i , end=" ")
# print()
#
# #1~10
# for i in range(1,11):
#     print(i, end=" ")
# print()
# #건너뛰면서 출력
# for i in range(1,11,2) :
#     print(i, end=" ")
# print()

# 문제2 1~10 사이 짝수만 출력
for i in range(2,10,2):
    print(i , end=" ")
print()
print()
# 문제3 구구단
# 단을 가로로
for i in range(2,10):
    for j in range(1,10):
        print(str(i)+"*"+str(j)+"="+str(i*j), end=" ")
    print()
print("================================================================")

# 단을 세로로
for i in range(1,10):
    for j in range(2,10):
        print(j,"*" ,i ,"=" ,i*j, end=" ")
    print()