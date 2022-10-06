import turtle,random

def getXYS():
    x=random.randint(-150,150)
    y=random.randint(-150,150)
    size=random.randint(10,50)
    return x,y,size
koreanStr="나랏말싸미 듕귁에 달아 문자와로 서로 사맛디 아니할쎄"
colorList=["red","green","blue","black","magenta","orange","gray"]

turtle.shape('turtle')
turtle.setup(330,330)
turtle.screensize(300,300)
turtle.penup()
turtle.speed(5)

for ch in koreanStr:
    X,Y,S =getXYS()
    color=random.choice(colorList)
    turtle.goto(X,Y)
    turtle.pencolor(color)
    turtle.write(ch,font=('맑은 고딕',S,'bold'))
