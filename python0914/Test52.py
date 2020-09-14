'''
파일입출력
#쓰기
1.open file
2.write
3.close file

#1 파일생성 : open("파일이름",파일열기모드)
    #2 mode
        r : 읽기
        w : 쓰기 ( 덮어쓰기 )
        a : 추가 ( 이어쓰기 )
#3 파일닫기 : 객체
'''
import codecs
def memory(msg):
    #open file
    file =codecs.open("database.txt","a","UTF-8")
    file.write(msg+"\n")
    file.close()
    #write
    #close file

def memory2(msg) :
    with open("database.txt","a",encoding='UTF-8') as file:
        file.write(msg+"/nr")



if __name__ == "__main__":
    memory(input("저장할 글 입력 : "))