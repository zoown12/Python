import turtle
import random

turtle.shape("turtle")
turtle.pensize(5)
turtle.pencolor("blue")

turtle.screensize(300,300)
turtle.setup(330,330)

while True:
    angle=random.randint(0,360)
    distance=random.randint(10,100)
    turtle.right(angle)
    turtle.forward(distance)
    curX=turtle.xcor()
    curY=turtle.ycor()

    if  (curX>=-150 and curX<=150) and (curY>=-150 and curY<=150):
        print("Good Boy")
    else:
        print("NO!!!")
        turtle.goto(0,0)
        
turtle.done()
