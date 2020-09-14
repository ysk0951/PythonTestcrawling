from tkinter import *
# 컨테이너

window = Tk()
def test():
    print("확인버튼 클릭")
# 컴포넌트
b1 = Button(window, text="확인", fg = "blue", command =test)
b2 = Button(window, text="종료", fg = "red", command= window.quit)

# 배치관리자
b1.pack(side=LEFT, fill=BOTH, padx = 10,pady=5,expand=YES)
b2.pack(side=RIGHT, fill=BOTH, padx = 10,pady=5,expand=YES)

# 계속 이벤트 리스닝
window.mainloop()