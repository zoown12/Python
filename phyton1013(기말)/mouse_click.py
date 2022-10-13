from tkinter import *
from tkinter import messagebox

#함수 선언부
def clickLeft(event):
    messagebox.showinfo("마우스","왼쪽 마우스가 클릭됨")
def clickRight(event):
    messagebox.showinfo("마우스","오른쪽 마우스가 클릭됨")

#메인 코드부
root = Tk()

root.bind("<Button-1>",clickLeft)
root.bind("<Button-3>",clickRight)

root.mainloop()
