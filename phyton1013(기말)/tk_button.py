from tkinter import *
from tkinter import messagebox

##함수 선언부
def myFunc1():
    messagebox.showinfo("버튼 클릭","버튼을 눌렀군요^^")

def myFunc2():
    messagebox.showinfo("삭제하기","삭제 완료!!")

##메인 코드부
root=Tk()
root.geometry('300x100')

button1=Button(root,text="클릭하세요",fg="red",command=myFunc1)
button1.pack()

button2=Button(root,text="삭제하기",fg="red",command=myFunc2)
button2.pack()

root.mainloop()
