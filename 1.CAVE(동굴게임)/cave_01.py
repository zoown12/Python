""" cave - Copyright 2016 Kenichiro Tanaka  """
import sys
from random import randint
import random
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE,K_UP,K_DOWN

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()

def main():
    """ 메인 루틴 """
    color="green"
    colorlist=["red","green","black","blue","magenta","orange","gray"]
    walls = 80
    ship_y = 250
    velocity = 0
    score = 0
    slope = randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("ship.png")
    bang_image = pygame.image.load("bang.png")
    rock_image = pygame.image.load("rock.png")
    holes = []
    for xpos in range(walls): #게임 시작시 동굴을 구성하는 직사각형 만들기
        holes.append(Rect(xpos * 10, 100, 10, 400))
    game_over = False

    while True:
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if not game_over:
                    if event.key ==K_UP:
                        ship_y-=2
                    if event.key ==K_DOWN:
                        ship_y+=2
        # 내 캐릭터를 이동
        if not game_over:
            score += 10 #점수 증가
            #velocity += -3 if is_space_down else 3
            velocity==0
            ship_y += velocity

            # 동굴을 스크롤
            edge = holes[-1].copy() #동굴을 이루는 오른쪽 끝 직사각형 복사
            test = edge.move(0, slope)#slope 값만큼 위 또는 아래로 조각을 이동
            if test.top <= 0 or test.bottom >= 600: #동굴 조각이 화면 끝에 도달하면
                slope = randint(1, 6) * (-1 if slope > 0 else 1)#방향과 값 수정
                edge.inflate_ip(0, -20)#동굴폭을 20만큼 감소시켜서 동굴이 좁아짐
                
            edge.move_ip(10, slope)#오른쪽 끝 조각의 바로 오른쪽 위치 이동
            holes.append(edge)#맨 끝에 edge를 추가(한 조각이 많아짐)
            del holes[0]#맨 앞 직사각형 삭제(조각의 수 일정하게 유지)
            holes = [x.move(-10, 0) for x in holes]# 전체 조각을 10 왼쪽방향

            # 충돌?
            if holes[0].top > ship_y or \
                holes[0].bottom < ship_y + 80: #동굴 바닥부분 충돌 검사,#동굴 윗부분 충돌검사
                game_over = True #충돌시 게임오버

        # 그리기
        SURFACE.fill(color)
        if score % 1000 ==0:
            color=random.choice(colorlist)
        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole) #검은색 동굴 표시
        SURFACE.blit(ship_image, (0, ship_y)) # 비행기 표시
        score_image = sysfont.render("score is {}".format(score),
                                     True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 20)) #점수 표시

        if game_over:
            SURFACE.blit(bang_image, (0, ship_y-40))

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__': 
    main()
