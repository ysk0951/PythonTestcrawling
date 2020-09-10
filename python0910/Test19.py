# 파라미터와 인자 : 개수 , 순서*가 일치해야한다.
# 인자를 기입할때, 파라미터=값
def signUp(username, pw, name, gender, email, addr, nation="S.Korea"):
    print("username",username)
    print("pw",pw)
    print(name)
    print(gender)
    print(email)
    print(addr)
    print(nation)

signUp("global","1234","피카츄","mail","pika@gmail.com","관악구","Korea")
