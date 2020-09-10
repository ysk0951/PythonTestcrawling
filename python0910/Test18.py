# 함수 : 파라미터와 인자 : 개수*와 순서가 일치해야함.
# 파라미터의 초기값 넣어주기 : 초기값 있는 파라미터는 파라미터들중 가장 뒤에 위치해야함

def signUp(username, pw, name, gender, email, addr, nation="S.Korea"):
    print("username",username)
    print("pw",pw)
    print(name)
    print(gender)
    print(email)
    print(addr)
    print(nation)

signUp("global","1234","피카츄","mail","pika@gmail.com","관악구","Korea")