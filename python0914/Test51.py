from importlib.metadata import files
from tkinter import *
# 컨테이너

window = Tk()
r2d2 = PhotoImage(file = "1.gif")
msg = """
이미지는 gif와 ppm/pgm포맷만 사용가능하다
특정 다른 모듈을 사용하면 다른 포맷의 이미지를 사용 가능
"""
lab = Label(window,image=r2d2).pack(side=RIGHT)
lab1 = Label(window,padx=10,text=msg).pack(side=LEFT)



# 계속 이벤트 리스닝
window.mainloop()