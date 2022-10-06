import turtle,random
colorList=["red","green","blue","black","magenta","orange","gray"]
turtle.shape('turtle')
turtle.setup(550,550)
turtle.screensize(500,500)
turtle.pensize(5)
turtleFile=open("C:/Users/user/Desktop/python0/trace.txt","w")
for i in range(30):
    x=random.randint(-250,250)
    y=random.randint(-250,250)
    color=random.choice(colorList)
    turtle.pencolor(color)
    turtle.goto(x,y)
    outStr=str(x)+" "+str(y)+" "+color+"\n"
    turtleFile.writelines(outStr)#파일 저장
turtleFile.close()
turtle.reset()#화면 지우기
turtle.pensize(5)
turtleFile=open("C:/Users/user/Desktop/python0/trace.txt","r")
while True:
    inStr=turtleFile.readline()
    if inStr=="":
        break
    x,y,color=inStr.split()# 값 분리 저장
    turtle.pencolor(color)
    turtle.goto(int(x),int(y))
turtleFile.close()
