'''
파이썬 -Oracle DB 연동
#라이브러리
    cx-Oracle(pycharm)
    cx-oracle(pip)

'''
import cx_Oracle

connection = cx_Oracle.connect("java06/java06@nullmaster.iptime.org:3000/orcl")
print('{}'.format(connection.version))
