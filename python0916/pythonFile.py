'''
파이썬 -Oracle DB 연동
#라이브러리
    cx-Oracle(pycharm)
    cx-oracle(pip)

'''
import cx_Oracle

# cx_Oracle.init_oracle_client(lib_dir='c:\oracle\instantclient_11_2')
connection = cx_Oracle.connect("java06/java06@nullmaster.iptime.org:3000/orcl")
print('{}'.format(connection.version))

cursor = connection.cursor()
cursor.execute("select * from test")
for c in cursor:
    print(c)


