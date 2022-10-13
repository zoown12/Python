import turtle,random
from PIL import Image

colorList=["red","green","black","blue","magenta","orange","gray"]
turtle.shape('turtle')
turtle.setup(850,850)
turtle.screensize(800,800)
turtle.speed(0)
turtle.penup()

for num in range(1,37,1):
    turtle.goto(0,0)
    turtle.right(10)
    turtle.forward(350)
    turtle.pencolor(random.choice(colorList))
    turtle.write(str(num),font=('맑은고딕',20,'bold'))

turtle.goto(0,0)
turtle.pendown()
turtle.pensize(5)

angle=random.randint(10,360) //10*10
turtle.right(angle)
turtle.forward(350)
number=angle//10
if number<10:
    number='0'+str(number)
else:
    number=str(number)

filename="C:/photo/picture"+number+".jpg"
img=Image.open(filename)
img.show()
