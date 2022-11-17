""" blocks.py - Copyright 2016 Kenichiro Tanaka """
import sys
import math
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect
score=0
width=180
stage=1

class Block:
    """ 블록, 공, 패들 오브젝트 """
    def __init__(self, col, rect, speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270

    def move(self):
        """ 공을 움직인다 """
        self.rect.centerx += math.cos(math.radians(self.dir))\
             * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir))\
             * self.speed
        
    def move2(self):
        """ 공을 움직인다 """
        self.rect.centerx += math.cos(math.radians(self.dir))\
             * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir))\
             * self.speed

    def draw(self):
        """ 블록, 공, 패들을 그린다 """
        if self.speed == 0:
            pygame.draw.rect(SURFACE, self.col, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.col, self.rect)
            
    def draw2(self):
        """ 블록, 공, 패들을 그린다 """
        if self.speed == 0:
            pygame.draw.rect(SURFACE, self.col, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.col, self.rect)

def tick():
    """ 프레임별 처리 """

    global score,width,stage
    global BLOCKS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                PADDLE.rect.centerx -= 10
            elif event.key == K_RIGHT:
                PADDLE.rect.centerx += 10
    if BALL.rect.centery < 1000:
        BALL.move()
        BALL2.move()

    # 블록과 충돌?
    prevlen = len(BLOCKS) #블록의 갯수만큼 
    BLOCKS = [x for x in BLOCKS
              if not x.rect.colliderect(BALL.rect)]
    if len(BLOCKS) != prevlen:
        BALL.dir *= -1
        score+=100

        if score%500==0:
            width-=30
            
    prevlen = len(BLOCKS) #블록의 갯수만큼 
    BLOCKS = [x for x in BLOCKS
              if not x.rect.colliderect(BALL2.rect)]
    if len(BLOCKS) != prevlen:
        BALL2.dir *= -1
        score+=100

        if score%500==0:
            width-=30

    # 패들과 충돌? #90도를 기준으로 패들의 센터 - 공의 센터
    if PADDLE.rect.colliderect(BALL.rect):
        BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) \
            / PADDLE.rect.width * 80

    if PADDLE.rect.colliderect(BALL2.rect):
        BALL2.dir = 90 + (PADDLE.rect.centerx - BALL2.rect.centerx) \
            / PADDLE.rect.width * 80

    # 벽과 충돌?
    if BALL.rect.centerx < 0 or BALL.rect.centerx > 600:
        BALL.dir = 180 - BALL.dir
    if BALL.rect.centery < 0:
        BALL.dir = -BALL.dir
        BALL.speed = 15

    if BALL2.rect.centerx < 0 or BALL2.rect.centerx > 600:
        BALL2.dir = 180 - BALL2.dir
    if BALL2.rect.centery < 0:
        BALL2.dir = -BALL2.dir
        BALL2.speed = 15



def paint(message):
    score_image = sysfont.render("score is {}".format(score),
                                     True, (0, 0, 225))
    SURFACE.blit(score_image,(600,15))
    
    width_image = sysfont.render("width {}".format(width),
                                     True, (0, 0, 225))
    SURFACE.blit(width_image,(600,50))
    
    stage_image = sysfont.render("stage  {}".format(stage),
                                     True, (0, 0, 225))
    SURFACE.blit(stage_image,(600,90))
    

pygame.init()
pygame.key.set_repeat(15, 15)
SURFACE = pygame.display.set_mode((900, 1000))
FPSCLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 36)
BLOCKS = []
PADDLE = Block((242, 242, 0), Rect(230, 700, 160, 30))
BALL = Block((242, 242, 0), Rect(300, 400, 20, 20), 10) # 공속도=10
BALL2 = Block("red", Rect(300, 400, 20, 20), 5) # 공속도=5
message=None
F_score=0

def main():
    """ 메인 루틴 """
    global message,F_score
    myfont = pygame.font.SysFont(None, 80)
    mess_clear = myfont.render("Cleared!", True, (255, 255, 0))
    mess_over = myfont.render("Game Over!", True, (255, 255, 0))
    fps = 30
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
              (0, 128, 0), (128, 0, 128), (0, 0, 250)]

    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0, 5):
            BLOCKS.append(Block(color,
                                Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30))) #80,30 블록의 크기


    while True:
        tick()

        if score>F_score and score%500==0:
            if PADDLE.rect.width>40:
                PADDLE.rect.inflate_ip(-30,0)
            F_score = score

        SURFACE.fill((0, 0, 0))
        BALL.draw()
        BALL2.draw2()
        PADDLE.draw()
        for block in BLOCKS:
            block.draw()

        if len(BLOCKS) == 0:
            SURFACE.blit(mess_clear, (200, 400))
        if BALL.rect.centery > 800 and len(BLOCKS) > 0:
            SURFACE.blit(mess_over, (150, 400))

            
        paint(message)
        pygame.display.update()
        FPSCLOCK.tick(fps)

if __name__ == '__main__':
    main()
