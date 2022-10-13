from tkinter import *
root = Tk()

button1=Button(root,text="버튼1")
button2=Button(root,text="버튼2")
button3=Button(root,text="버튼3")

button1.pack(side=BOTTOM,fill=X,padx=10,pady=10)#TOP,RIGHT,LEFT,BOTTOM
button2.pack(side=BOTTOM,fill=X,padx=10,pady=10)#NONE:확장하지 않음,X-수평,Y-수직,BOTH-수평수직둘다
button3.pack(side=BOTTOM,fill=X,padx=10,pady=10)

root.mainloop()
