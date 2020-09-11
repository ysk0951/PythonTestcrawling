'''
매개변수의 종류:
일반 매개변수,
*args,
    매개변수=초기값
**kwargs
    함수 호출시 , 몇개가 될지 모르는
    key=value 쌍으로 이루어진 인자들을
    한번에 받아주기 위한 파라미터
    초기화 파라미터전에 와야함
    **kwargs << a=10 , b=20, play=True,lst=[1,2,3,4,5]
'''
def packer(name,**kwargs):
    print(name)
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.items())

# packer("pika",age=30,mobile="010-1234-4567",city="Seoul")

def unpacker(name=None,score=0) :
    print("%s의 점수는 %d점 입니다." %(name,score))
    #data 있으면 True취급
    # if name :
    #     print("%s의 점수는 %d점 입니다." %(name,score))
    # else :
    #     print("이름 또는 점수가 없습니다.")

unpacker(**{"score" : 100, "name":"pika"})