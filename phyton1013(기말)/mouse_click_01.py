from tkinter import *

def clickMouse(event):
    if event.num==1:
        txt="왼쪽 버튼:("+str(event.x)+","+str(event.y)+")"
    elif event.num==3:
        txt="오른쪽 버튼:("+str(event.x)+","+str(event.y)+")"

    label1.configure(text=txt)

root=Tk()
root.geometry("400x400")

label1=Label(root,text="여기가 바뀝니다.",fg="red")
label1.pack(expand=YES,anchor=CENTER)

root.bind("<BUTTON>",clickMouse)

root.mainloop()
