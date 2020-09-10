# 문제1. 문자열 인덱싱 + if
'''
주민번호를 입력받아,
여성, 남성을 판단하는 프로그램을 만들어보세요.
예) 800101-1002222     남성 1,3  여성 2,4
'''
# num = input("주민번호 입력하세요 : ")
# print(num[7])
# if num[7]%2==0:
#     print("남성")
# else :
#     print("여성")

#문제2.사용자로 부터 키(height)를 입력받는다.
#       입력받은 키가 140 이상이면 "놀이기구 이용가능해~~" 출력
#       입력받은 키가 140 미만이면 , 질문 : "부모님이랑 왔니? yes:1, no:0 "
#               답변 : 1 -> 이용가능해~ 재밌게 놀아라~~~ 출력
#               답변 : 0 -> 부모님 모시고 다시 오렴~~~  출력
# height = int(input("height 입력하세요 : "))
# if height>=140:
#     print("놀이기구 이용가능해~~")
# elif  height<140:
#     option = int(input("부모님이랑 왔니? yes:1, no:0 """))
#     if option == 1:
#         print("이용가능해~ 재밌게 놀아라~~~")
#     elif option == 0:
#         print("부모님 모시고 다시 오렴~~~")

#문제3. 학점 처리 프로그램
'''
이름, 국어점수, 영어점수, 수학점수 4가지를 입력받고, 
총점, 평균, 학점을 구해보세요.
단, 평균은 소수점 이하 한자리까지 표현
학점 : 평균 90이상 A
    80이상 B
    70이상 C
    60이상 D
    이하 F
'''
# name = input("이름 입력하세요 : ")
# kor = int(input("국어점수 입력하세요 : "))
# eng = int(input("영어점수 입력하세요 : "))
# math = int(input("수학점수 입력하세요 : "))
#
# tot = kor+eng+math
# avg = tot/3.0
# grade = ''
# if avg >=90:
#     grade = 'A'
# elif avg >=80:
#     grade = 'B'
# elif avg >=70:
#     grade = 'C'
# elif avg >=60:
#     grade = 'D'
# else :
#     grade = 'F'
# print("이름은 {} 이고 총점은 {} 이고 평균은 %0.1f이고 학점은 {}입니다." .format(name,tot,grade) %avg)
####### while #######
#문제4. 0 ~ 3 까지 출력
# i = 0
# while i<=3 :
#     print(i)
#     i += 1

#문제5. 1 ~ 10 사이 홀수 출력
# i = 1
# while i<10:
#     print(i)
#     i +=2

#문제6. 0 ~ 100 사이 10단위로 출력    ex) 0 10 20 30 ...
# i = 0
# while i<=100:
#     print(i)
#     i+=10

#문제7. 1 ~ 10 까지 총합 출력
# i=1
# count = 0
# while i<=10 :
#     count += i
#     i+=1
# print(count)

#문제8. 1 ~ 20 까지 짝수의 총합 출력
# i=1
# count = 0
# while i<=20 :
#     if i%2==0 :
#         count += i
#     i+=1
# print(count)
#문제9. 숫자 5번 입력받고, 입력받을때마다 입력된 수의 누적합계를 출력
# count = 0
# tot = 0
# while count<5:
#     tot += int(input("숫자를 입력하세요 :"))
#     print("누적합계 :"+str(tot))
#     count+=1
#문제10. 카페 주문프로그램
'''
*** global 카페 메뉴 ***
1. 아메리카노 : 2000원
2. 카페 라떼 : 2500원
3. 에스프레소 프라푸치노 : 4000원
4. 베이글+크림치즈 : 4500원
5. 종료
원하는만큼 주문받고, 종료시 총액 출력
'''
# select=-1
# tot = 0
# while select!=5:
#     print(
#      '''*** global 카페 메뉴 ***
#  1. 아메리카노 : 2000원
#  2. 카페 라떼 : 2500원
#  3. 에스프레소 프라푸치노 : 4000원
#  4. 베이글+크림치즈 : 4500원
#  5. 종료 '''
#     )
#     select = int(input("숫자를 입력하세요 :"));
#     if select == 1:
#         tot += 2000
#     elif select == 2:
#         tot += 2500
#     elif select == 3:
#         tot += 4000
#     elif select == 4:
#         tot += 4500
# print("총금액 : "+str(tot)+"원입니다")
# 문제11. ATM 기계
'''
*** Global ATM ***
1. 입금
2. 출금
3. 잔액조회
4. 계좌이체
5. 종료

1단계 : 메뉴 번호 선택하면, 메뉴 이름 출력
2단계 : 메뉴별 기능 구현 money = 100000
3단계 : 아이디/패스워드 받아, 로그인하면 서비스 이용가능하게
4단계 : 아이디/패스워드 3번 오류시 프로그램 강제 종료
추가....
'''
money = 100000
select = -1
result = True
cookie = False
errorcount = 0
dbid = "python"
dbpw = "1234"
id = ''
pw = ''
while select != 5 or result != True:
    if not cookie :
        id =input("id를 입력해주세요")
        pw =input("pw를 입력해주세요")
    if id!=dbid or pw!=dbpw:
        result = False
        errorcount += 1
        print("로그인에 실패하셨습니다")
        if errorcount == 3:
            print("로그인에 3번 실패하셨습니다 강제종료합니다")
            break
    else:
        key = True
        errorcount = 0
        print('''*** Global ATM ***
1. 입금
2. 출금
3. 잔액조회
4. 계좌이체
5. 종료''')
        select = int(input("메뉴번호를 입력하세요 :"))
        if select==1:
            add = int(input("입금액을 입력하세요 :"))
            money+=add
        if select==2:
            sub = int(input("출금액을 입력하세요 :"))
            money -= sub
        if select==3:
            print("잔액은 {} 입니다" .format(money))
        if select==4:
            print("계좌이체입니다")
        if select == 5:
            print("프로그램을 종료합니다")