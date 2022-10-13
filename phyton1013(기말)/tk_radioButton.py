from tkinter import *

def myFunc():
    if myVar.get()==1:
        label1.configure(text="벤츠")
    elif myVar.get()==2:
        label1.configure(text="BMW")
    elif myVar.get()==3:
        label1.configure(text="아우디")
    elif myVar.get()==4:
        label1.configure(text="재규어")

root=Tk()
root.geometry('300x200')

myVar=IntVar()#Tkinter 에서 사용할 수 있는 정수형 객체 생성
rb1=Radiobutton(root,text="벤츠",variable=myVar,value=1,command=myFunc)
rb1.pack()
rb2=Radiobutton(root,text="BMW",variable=myVar,value=2,command=myFunc)
rb2.pack()
rb3=Radiobutton(root,text="아우디",variable=myVar,value=3,command=myFunc)
rb3.pack()
rb4=Radiobutton(root,text="재규어",variable=myVar,value=4,command=myFunc)
rb4.pack()

label1=Label(root,text="선택한 차량:",fg="red")
label1.pack()

root.mainloop()

#label 컨트롤
#configure 컨트롤 옵션값 변경
#command 함수 지정
#variable 
