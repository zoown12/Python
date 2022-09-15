import turtle

turtle.shape('turtle')
turtle.pensize(5)
turtle.pencolor("blue")

while True:
    angle_right=int(input("거북이의 오른쪽회전각도:"))
    angle_left=int(input("거북이의 왼쪽회전각도:"))
    distance=int(input("거북이의 이동거리:"))

    turtle.left(angle_right)
    turtle.right(angle_left)
    turtle.forward(distance)
