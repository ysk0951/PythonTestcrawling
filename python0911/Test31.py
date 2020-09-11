'''

'''
menu='''
1. 학생정보 출력
2. 학생정보 입력
3. 학생정보 수정
4. 학생정보 삭제
5. 학생정보 검색
6. 총점, 평균
7. 종료
'''
scores = {"이영규":90,"박결":80,"박원용":70,"김영성":60}
while True:
    option = 0

    print(menu)
    option = int(input("메뉴번호 입력 : "))
    if option == 1:
        print(scores)
    if option == 2:
        name = input("학생이름 입력 : ")
        score = int(input("학생점수 입력 : "))
        scores[name] = score
        print(scores)
    if option == 3:
        name = input("학생이름 입력 : ")
        #일치여부
        keys = list(scores.keys())
        isExist = False
        for i in keys:
            if i==name:
                isExist=True

        if isExist:
            score = int(input("학생점수 입력 : "))
            scores[name] = score
        else :
            print("학생이 존재하지 않습니다")
        print(scores)
    if option == 4:
        name = input("학생이름 입력 : ")
        # 일치여부
        keys = list(scores.keys())
        isExist = False
        for i in keys:
            if i == name:
                isExist = True
        if isExist:
           scores.__delitem__(name)
        else:
            print("학생이 존재하지 않습니다")
        print(scores)
    if option == 5:
        name = input("학생이름 입력 : ")
        # 일치여부
        keys = list(scores.keys())
        isExist = False
        for i in keys:
            if i == name:
                isExist = True
        if isExist:
            print(name,"학생의 점수는 : ",scores.get(name))
        else:
            print("학생이 존재하지 않습니다")

    if option == 6:
        keys = list(scores.keys())
        tot  = 0
        cnt = 0
        for i in keys:
            tot+=scores.get(i)
            cnt+=1
        print("tot : ",tot,"/ ave : ",tot/cnt)
    if option == 7:
        print("프로그램 종료")
        break