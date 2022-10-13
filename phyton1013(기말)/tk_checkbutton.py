from tkinter import *
from tkinter import messagebox

def myFunc1():
    if chk.get() ==0:
        messagebox.showinfo("","체크버튼 OFF 네요.")
    else:
        messagebox.showinfo("","체크버튼 ON 이네요.")

root=Tk()
root.geometry('300x100')

chk=IntVar()#Tkinter 에서 사용할 정수형 객체 생성
cb1=Checkbutton(root,text="클릭하세오",variable=chk,command=myFunc1)
cb1.pack()

root.mainloop()
