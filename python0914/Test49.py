from tkinter import *
# 컨테이너

window = Tk()
# 컴포넌트
b1 = Button(window, text="one")
b2 = Button(window, text="two")
b3 = Button(window, text="three")
b4 = Button(window, text="병합하고 싶어요")
# 배치관리자
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0,columnspan=3)

# 계속 이벤트 리스닝
window.mainloop()