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

lst = [1,2,3,4,5]
lst[1] = ['a','b','c']
print(lst)
lst[1:2] = ['a','b','c']
print(lst)
lst[1]='a','b','c' #tuple
print(lst)
print(lst)

#1 요소추가하기 : .append
lst = []
lst.append(10)
lst.append(20)
print(lst)
#2 리스트확장
lst1 = [1,2,3]
lst2 = [4,5,6]
lst1.extend(lst2)
#print(lst1+lst2)와 동일
print(lst1)
#3. 요소 삽입하기 : insert(a,b) :a번째 위치에 b요소를 삽입
