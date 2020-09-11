'''
집합 set : value를 버리고 key만 남은 dict와 같은 형태(중복제거 집합)
- set
- 중복을 허용X
- 순서X
- 교집합 intersection 합집합 union 차집합 difference
- 구조
    변수명 = set(리스트, 문자열, 튜플, 딕셔너리)
'''

s1 = set([1,2,3,4,5,6,7])
s2 = set([3,6,8,9])

#교집합
print(s1 & s2)
print(s1.intersection(s2))
#차집합
print(s1-s2)
print(s1.difference(s2))
print(s2-s1)
print(s2.difference(s1))

#추가하기
s3 = set([1,2,3])
print(s3)
s3.add(100)
print(s3)

#삭제하기
s3.remove(100)
print(s3)