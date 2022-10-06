import turtle,random
class Rabbit:
    myTurtle =None
    def __init__(self,myTut):
        self.myTurtle=myTut
        print("**토끼가 거북이 등에 올라탔습니다.**")
    def print_my_position(self):
        print("거북이 등 위의 토끼 위치는 현재",
              self.myTurtle.xcor(),",",self.myTurtle.ycor(),"입니다.")
myTut,myRab=None,None
colorList=["red","green","blue","black","magenta","orange","gray"]

turtle.setup(550,550)
turtle.screensize(500,500)

myTut=turtle.Turtle("turtle")
myRab=Rabbit(myTut)
myTut.pensize(5)

for i in range(20):
    x=random.randint(-250,250)
    y=random.randint(-250,250)
    color=random.choice(colorList)
    myTut.pencolor(color)
    myTut.goto(x,y)
    myRab.print_my_position()
    
