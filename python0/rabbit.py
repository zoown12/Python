class Rabbit:
    shape=""
    xPos=0
    yPos=0

    def goto(self,x,y):
        self.xPos=x
        self.yPos=y

rabbit=None
userX,userY=0,0

rabbit=Rabbit()
rabbit.shape="토끼"

while True:
    userX+=int(input("토끼가 이동할 x좌표 ==>"))
    userY+=int(input("토끼가 이동할 y좌표 ==>"))
    rabbit.goto(userX,userY)
    print("**토끼의 현재 위치는 (",userX,",",userY,")")
