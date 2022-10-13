import pygame
import random
import sys

##전역변수부
Monitor=None
colorList=["red","green","black","blue","magenta","orange","gray"]

##메인 코드부
pygame.init()
pygame.key.set_repeat(5,5)
monitor=pygame.display.set_mode((500,700))
color=random.choice(colorList)
turtle=pygame.image.load("C:/Temp/turtle.png")
tx,ty=200,300
while True:
    monitor.fill(color)
    monitor.blit(turtle,(tx,ty))
    pygame.display.update()
    for e in pygame.event.get():
        if e.type in [pygame.QUIT]:
            pygame.quit()
            sys.exit()
        if e.type in [pygame.KEYDOWN]:
            if e.key == pygame.K_LEFT:tx-=5
            elif e.key == pygame.K_RIGHT:tx+=5
            elif e.key == pygame.K_UP:ty-=5
            elif e.key == pygame.K_DOWN:ty+=5
        if e.type in [pygame.KEYDOWN]:
            if e.key == pygame.K_SPACE:
                tx=random.randint(0,500)
                ty=random.randint(0,700)
