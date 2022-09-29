import turtle
import random

turtleList=[]
colorList=["red","green","blue","black","magenta","orange","gray"]
shapeList=["arrow","circle","square","triangle","turtle"]

turtle.setup(550,550)#윈도우크기
turtle.screensize(500,500)

for i in range(0,100):
    shape=random.choice(shapeList)
    color=random.choice(colorList)
    x=random.randint(-250,250)
    y=random.randint(-250,250)
    myTurtle=turtle.Turtle(shape)
    tup=(myTurtle,color,x,y) #거북이 모양/색상/위치 튜플저장
    turtleList.append(tup)#리스트에 저장
for tup in turtleList:#저장된 값을 이용해 100마리 그리기
    myTurtle=tup[0]
    myTurtle.pencolor(tup[1])
    myTurtle.goto(tup[2],tup[3])

turtle.done()
