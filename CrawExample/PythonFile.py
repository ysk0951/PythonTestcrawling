'''
파이썬 -Oracle DB 연동
#라이브러리
    cx-Oracle(pycharm)
    cx-oracle(pip)

'''
import cx_Oracle
import datetime

#cx_Oracle.init_oracle_client(lib_dir='c:\oracle\instantclient_11_2')
connection = cx_Oracle.connect("java06/java06@nullmaster.iptime.org:3000/orcl")
print('{}'.format(connection.version))
cursor = connection.cursor()

# #레코드 1개 삽입
# sql = 'insert into test values(:1,:2,:3,:4)'
# data = ('patyon1234','0000',20,datetime.datetime.now())
# cursor.execute(sql,data)
# connection.commit()
#

# 여러 레코드 삽입 방식1
# users = [
#     ('patyon1','0000',20,datetime.datetime.now()),
#     ('patyon2','0000',20,datetime.datetime.now()),
#     ('patyon3','0000',20,datetime.datetime.now()),
#     ('patyon4','0000',20,datetime.datetime.now())
# ]
# sql = 'insert into test values(:1,:2,:3,:4)'
#
# for u in users:
#     cursor.execute(sql,u)
#
# cursor.close()
# connection.commit()
# connection.close()

# # 여러 레코드 삽입 방식2
# users = [
#     ('py1','0000',20,datetime.datetime.now()),
#     ('py2','0000',20,datetime.datetime.now()),
#     ('py3','0000',20,datetime.datetime.now()),
#     ('py4','0000',20,datetime.datetime.now())
# ]
# sql = 'insert into test values(:1,:2,:3,:4)'
#
# #DB에 저장시킬 레코드의 개수 cursor에 세팅
# cursor.arraysize = len(users)
# #한방에 실행
# cursor.executemany(sql,users)
# cursor.close()
# connection.commit()
# connection.close()

# #결과물 추출
# query = 'select * from test'
# cursor.execute(query)
# for c in cursor:
#     print(c)

# 전체 데이터 조회
sql = "select count(*) from test"
cursor.execute(sql)
count = cursor.fetchone()
print(count[0])
print(type(count))

#데이터 수정
# sql = "update test set pw='123' where id = 'test1'"
# cursor.execute(sql)
# cursor.close
# connection.commit()
# connection.close

# id = input("아이디 입력")
# new_pw = input("새 비밀번호 입력 : ")
#
# sql = "update test set pw=:1 where id =:2"
# data = (new_pw,id)
# cursor.execute(sql,data)
# cursor.close()
# connection.commit()
# connection.close

# 데이터 삭제
sql = "delete from test where id = :1"
data = ('py2',)
cursor.execute(sql,data)
connection.commit()
connection.close()










# #닫기
# cursor.close()
# connection.close()


