'''
 모듈, 패키지
 1) 모듈

 import 모듈명
 import 패키지명.모듈명
 import python0911.Test30

#abc.py(패키지X)
name = "피카츄"
def sleep()
    pass
def eat()
    pass

# test.py에서 abc.py import
import abc
abc.sleep()
abc.eat
abc.name

이렇게 쓸수있음
from abc import *
sleep()

#디렉토리 내에서 모듈찾음
#PythonPath 환경변수에 지정된 디렉토리에서 찾음
#Python Lib에서 디렉토리를 찾음

#-----------------------------------------
# tkinter
# GUI 프로그램 개발시 사용하는 모듈
1) 컨테이너
2) 컴포넌트
3) 배치관리자
4) 이벤트

배치관리자 3가지
1) pack 상하좌우 배치
2) grid 행/열로 배치
3) place 좌표로 배치

#pack
    - side : 위젯을 배치하는 시작점설정 Top Left Right Bottom
    - fill : 위젯을 화면에 꽉차게 표시
    - expand : 창의 크기가 변하면 위젯의 배치도 비율대로 변함
    - padx / pady : 좌우/상하 여백지정
    - anchor : 위젯을 범위에 따라 배치
        E W S N SW SE NW NE
'''
from tkinter import *

window = Tk()
b1 = Button(window, text="one")
b1.pack()
window.mainloop()