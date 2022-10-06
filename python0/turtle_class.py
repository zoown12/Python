import turtle
class SeaTurtle(turtle.Turtle):
    name=''
    body=None
    def __init__(self):
        self.body=turtle.Turtle('triangle')
        self.body.color("blue")
        self.name='바다거북'
    def swim(self,x,y):
        self.body.goto(x,y)

class SandTurtle(turtle.Turtle):
    name=''
    body=None
    def __init__(self):
        self.body=turtle.Turtle('circle')
        self.body.color("red")
        self.name='모래거북'
    def walk(self,x,y):
        self.body.goto(x,y)
setTut,sandTut =None,None
seaTut=SeaTurtle()
sandTut=SandTurtle()
seaTut.swim(100,100)
seaTut.body.write(seaTut.name,font=("Arial",20))
sandTut.walk(-100,100)
sandTut.body.write(sandTut.name,font=("Arial",20))
    
