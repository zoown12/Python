import turtle
import random

turtle.shape("turtle")
colors=['red','green','magenta','blue','black']
turtle.penup()
turtle.screensize(300,300)
turtle.setup(330,330)

for i in range(7):
    for k in range(7):
        x=i*50-150 #기준점이 0 0 -150이 시작값
        y=k*50-150  
        turtle.goto(x,y)
        turtle.color(random.choice(colors))
        turtle.stamp()
        
turtle.done()
