# '''
# 딕셔너리 dict
# key value 쌍으로 이루어진 데이터들이 저장되는 공간
# 수정가능 mutable
# 구조
#     변수명 = {key:value , key:value,...}
#
# '''
#
# dic = {"a" : 10, "b":"hahaha","c":True}
# print(dic)
# print(dic["a"])
#
# dic = {}
# print(type(dic))
#
info = {"mob" : "010-1111-2222", "age" : 10, "name" : "토르"}
#
# #keys()
# keys = info.keys()
# #dict_keys(['mob', 'age', 'name'])
# print(type(keys))
# print(list(keys))
# #key는 list로 형변환 하거나 for로 꺼내야함
# for i in keys:
#     print(i)
# #values()
# values = info.values()
# print(values)
# items = info.items()
# print(items)
# print("-----------------")
# age = info.get("age")
# print(age)
# city = info.get("city",[1,2,3])
# print(city)
# print("city" in info)
#
# info.update({"city" : "seoul"})
# print(info)
# info["addr"] = "관악구"
# print(info)
#
# # dict의 값 변경 : update()
# info.update({"city" : "busan"})
# print(info)
#  dict 요소 제거
# info["addr"] = "서초구"
# info.__delitem__("addr")
# print(info)
