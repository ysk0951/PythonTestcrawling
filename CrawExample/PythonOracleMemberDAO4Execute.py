import cx_Oracle
import datetime

class PythonOracleMemberDAO:
    connection = cx_Oracle.connect("java06/java06@nullmaster.iptime.org:3000/orcl")
    cursor = connection.cursor()
    # 회원 조회
    def selectOne(slef):
        data = (input('[조회할 회원의 아이디를 입력하세요] : '),)
        print(data,type(data))
        sql = 'select * from member where id = :1'
        slef.cursor.execute(sql,data)
        for c in slef.cursor:
            print(c)
        print("test3")
    # 회원 전체조회
    def selectAll(slef):
        pass
    # 회원 삽입
    def selectInsert(slef):
        pass
    # 회원 비번 수정
    def selectUdatePassword(slef):
        pass
    # 회원 삭제
    def selectDelete(slef):
        pass
    # 회원 아이디/비번확인
    def selecIdPw(slef):
        pass
