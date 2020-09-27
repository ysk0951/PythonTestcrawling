import cx_Oracle
import datetime
 
class PythonOracleMemberDAO:
    connection = None
    cursor = None
    def con_open(self):
        self.connection = cx_Oracle.connect("java06/java06@nullmaster.iptime.org:3000/orcl")
        self.cursor = self.connection.cursor()
    def con_close(self):
        self.connection = None
        self.cursor = None
    # 회원 조회
    def selectOne(slef):
        slef.con_open()
        data = (input('[조회할 회원의 아이디를 입력하세요] : '),)
        sql = 'select * from member where id = :1'
        slef.cursor.execute(sql,data)
        for c in slef.cursor:
            print(c)
        slef.con_close()
    # 회원 전체조회
    def selectAll(slef):
        slef.con_open()
        sql = 'select * from member'
        slef.cursor.execute(sql)
        for c in slef.cursor:
            print(c)
        slef.con_close()
    # 회원 삽입
    def selectInsert(slef):
        slef.con_open()
        id = input('[회원의 아이디를 입력하세요] : ')
        pw = input('[회원의 비밀번호를 입력하세요] : ')
        name = input('[회원의 이름을 입력하세요] : ')
        sql = 'insert into member values(:1,:2,:3,:4,:5,:6)'
        data = (id,pw,name,datetime.datetime.now(),"python",datetime.datetime.now())
        slef.cursor.execute(sql,data)
        slef.connection.commit()
        slef.con_close()
    # 회원 비번 수정
    def selectUpdatePassword(slef):
        slef.con_open()
        id = input('[회원의 아이디를 입력하세요] : ')
        pw = input('[수정할 비밀번호 입력하세요] : ')
        sql = 'update member set pw=:1 where id = :2'
        data = (pw,id)
        slef.cursor.execute(sql, data)
        print("update완료")
        slef.connection.commit()
        slef.con_close()
    # 회원 삭제
    def deleteMember(slef):
        slef.con_open()
        id = input('[삭제 회원의 아이디를 입력하세요] : ')
        sql = 'delete member where id=:1'
        data = (id,)
        slef.cursor.execute(sql, data)
        print("delete완료")
        slef.connection.commit()
        slef.con_close()

    # 회원 아이디/비번확인
    def selecIdPw(slef):
        slef.con_open()
        data = (input('[조회할 회원의 아이디를 입력하세요] : '),)
        sql = 'select pw from member where id = :1'
        slef.cursor.execute(sql, data)
        for c in slef.cursor:
            print(c)
        slef.con_close()
