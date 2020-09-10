#문제2 : 로그인 프로그램
"""
사용자로부터 id와 pw를 입력받아,
일치하는 id가 없을 경우,
"존재하지 않는 id입니다"
id는 존재하지만 pw가 틀릴경우, "비밀번호가 틀렸습니다"
둘다 일치할경우, "(id)님 환영합니다"
"""
# db_id = "korea"
# db_pw = "1234"
#
# id = input("id를 입력하세요 :")
# pw = input("pw를 입력하세요 :")
# if id != db_id :
#     print("존재하지 않는 id입니다")
# elif pw != db_pw :
#     print("비밀번호가 틀렸습니다")
# else :
#     print(db_id,"님 환영합니다")
# 문제3. ATM 기계 >> 각 메뉴별 기능을 함수로 변경. + 로그인 기능 추가
'''
*** Global ATM ***
1. 입금
2. 출금
3. 잔액조회
4. 계좌이체
5. 종료
'''

''''''
money = 100000
select = -1
result = True
cookie = False
errorcount = 0
dbid = "python"
dbpw = "1234"
id = ''
pw = ''

def deposit(add):
    global money
    money = money+add
def withdraw(sub):
    global money
    money = money-sub
def balance_inquiry():
    global money
    print("잔액은",money,"입니다")
def remittance(remiitance):
    global money
    money -= remiitance
    print("계좌이체후 잔액은",money,"입니다")
def login():
    while True:
        id = input("id를 입력해주세요")
        pw = input("pw를 입력해주세요")
        if id != dbid or pw != dbpw:
            result = False
            global  errorcount
            errorcount += 1
            print("로그인에 실패하셨습니다")
            if errorcount == 3:
                print("로그인에 3번 실패하셨습니다 강제종료합니다")
                return result
        else :
            result = True
            errorcount = 0
            print("로그인성공")
            return result

key = False
while select != 5 or result :
    #기존에 로그인 여부
    if(not key):
        print("로그인이 안되어있어 로그인을 진행합니다.")
        result = login()
        if(result):
            key = True
    print('''*** Global ATM ***
1. 입금
2. 출금
3. 잔액조회
4. 계좌이체
5. 종료''')
    select = int(input("메뉴번호를 입력하세요 :"))
    if select == 1:
        add = int(input("입금액을 입력하세요 :"))
        deposit(add)
    if select == 2:
        sub = int(input("출금액을 입력하세요 :"))
        withdraw(sub)
    if select == 3:
        balance_inquiry()
    if select == 4:
        remit=int(input("계좌이체 금액을 입력하세요 :"))
        remittance(remit)
    if select == 5:
        print("프로그램을 종료합니다")
        break