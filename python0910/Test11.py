'''
리스트 list
    변수명 = [요소 , 요소, 요소, ...]
    다양한 데이터 타입 섞어서 저장가능
    수정가능 mutable
    크기제한 없다
    구분기호 : []
'''
# 빈 리스트
# a = []
# b = list()
# print(a)
# print(b)
# print(type(b))
# c = [1,2,3]
# print(c)
# d = [10,20,True,"list","python"]
# print(d)
# num = [1,2,3,4,5]
# print(num)
# print(num[2])
# num2 = [[1,2,3],[4,5,6],[7,8,9]]
# print(num2)
# print(num2[0][0])
#
# num3 = [1,2,3,[4,5,6],7]
# print(num3[3][0])
# print(num3[2])
# print(num3[4])
#
# num4 = [1,2,3,["A","B","C"],4,5]
# #1 [3,["A","B","C"],4]
# print(num4[2:5])
#
# #2 ["A","B"]
# print(num4[3][0:2])
# lst = [1,2,3]
# lst[0] = 100
# print(lst)

# lst = [1,2,3,4,5]
# lst[1] = ['a','b','c']
# print(lst)
# lst[1:2] = ['a','b','c']
# print(lst)
# lst[1]='a','b','c' #tuple
# print(lst)
# print(lst)

#1 요소추가하기 : .append
# lst = []
# lst.append(10)
# lst.append(20)
# print(lst)

#2 리스트확장
# lst1 = [1,2,3]
# lst2 = [4,5,6]
# lst1.extend(lst2)
#print(lst1+lst2)와 동일
# print(lst1)

#3. 요소 삽입하기 : insert(a,b) :a번째 위치에 b요소를 삽입
# lst = [1,2,3]
# lst.insert(1,4)
# print(lst)

#4. 요소 제거하기
# lst.remove(4)
# print(lst)

#문제1. 임의의 요소 5개 들어있는 리스트 하나 만들고,
#       인덱스번호 두개 입력받고 해당인덱스 번호에 자리한값을 교환해보자.
# lst_ = [1,2,3,4,5]
# num1 = int(input("0번 인덱스 입력 :"))
# num2 = int(input("1번 인덱스 입력 :"))
# tmp = lst_[num1]
# lst_[num1] = lst_[num2]
# lst_[num2] = tmp
# print(lst_)

# [5,4,3,2,1]로 바꾸기
# lst_ = [1,3,5,2,4]
# lst_.sort()
# lst_.reverse()
# print(lst_)

# in / not in
# lst = [10,20,30,'abc','def']
# if 10 in lst :
#     print("10이 존재한다")
# print("abc" not in lst)
#
# lst = [0]*5
# print(lst)
