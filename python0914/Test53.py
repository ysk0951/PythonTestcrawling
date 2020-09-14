'''
파일 읽기
1) 파일 열기 : open("파일이름","r")
2) read()
3) close()

'''

file = open("database.txt",encoding="UTF-8")
# rd = file.read(10) #읽어올 바이트수
# file.seek(0) #어디로 갈지 0== 처음
# print(rd)

# lines = file.readlines() #한줄씩 배열로 읽어와서 던져줌
# for line in lines:
#     print(line[::-1])

with open("database.txt","a",encoding='UTF-8') as file:
    lines = file.readlines()
    for line in lines:
        print(line)