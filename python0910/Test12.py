'''
# 반복문 for
    for 변수 in 군집자료형
    for index in "문자열" list tuple
'''
# for i in "hello":
#     print(i)
#     
# lst = [10,20,30,40,50]
# for i in lst:
#     print(i)
#     
'''
총 5명의 학생이 시험을 봤고
시험점수가 60이상이면 합격 미만은 불합격 출력
'''

#
score = [90,40,65,80,59]
num = 1
for i in score:
    if i >=60:
        print("%d번 학생의 점수는 %d점으로 합격" %(num,i))
    else :
        print("%d번 학생의 점수는 %d점으로 불합격"  %(num,i))
    num +=1