#한줄 주석

"""
여러줄주석
"""

'''
파이썬은 기본적으로 세미콜론이 없음
파이썬은 띄어쓰기, 들여쓰기 중요
'''
print("hello python!!!")
print("hello" , "python")

#option
print('test1', end=" ")
print('test2', end=" ")
print('test'*100)
print('='*100)

'''
Escape
\n
\t 
\'
포맷팅
1) % 포메팅
    숫자 : 정수 %d 실수 %f
    문자 : 문자1개 %c 문자1개 이상%s
    변수 : 변수안의 데이터 타입에 맞게
2) {} 포메팅

'''
print("나이는 %d살이고 이름은 %s입니다" %(10,"pica"))
print("이름은 %s입니다" %"pica")
print("키는 %.2f입니다" %200.8)
print("hello {} 시간입니다 {} testfile" .format("python","열심히"))