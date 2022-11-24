""" invader.py - Copyright 2016 Kenichiro Tanaka  """
import sys
from random import randint
import pygame
from pygame.locals import Rect, QUIT, KEYDOWN,KEYUP, K_LEFT, K_RIGHT, K_SPACE ,K_UP,K_DOWN

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()

class Drawable:
    """ 전체의 그리기 객체의 슈퍼 클래스 """
    def __init__(self, rect, offset0, offset1): 
        strip = pygame.image.load("strip.png")
        #빈 이미지 준비 크기 :24 x 24, 투명도 값을 포함 하도록 설정 
        self.images = (pygame.Surface((24, 24), pygame.SRCALPHA),
                       pygame.Surface((24, 24), pygame.SRCALPHA))
        self.rect = rect
        self.count = 0
        self.images[0].blit(strip, (0, 0), Rect(offset0, 0, 24, 24))
        self.images[1].blit(strip, (0, 0), Rect(offset1, 0, 24, 24))

    def move(self, diff_x, diff_y):
        """ 객체를 이동 """
        self.count += 1
        self.rect.move_ip(diff_x, diff_y)

    def draw(self):
        """ 객체를 그리기 """
        image = self.images[0] if self.count % 2 == 0 else self.images[1]
        SURFACE.blit(image, self.rect.topleft) 

class Ship(Drawable):
    """ 내 캐릭터 객체 """
    def __init__(self):
        super().__init__(Rect(300, 550, 24, 24), 192, 192) #x,y,크기, 위치(192)

class Beam(Drawable):
    """ 빔 객체 """
    def __init__(self):
        super().__init__(Rect(300, 0, 24, 24), 0, 24) #x,y,크기 , 0 48 96 144 192

class Bomb(Drawable):
    """ 폭탄 객체 """
    def __init__(self):
        super().__init__(Rect(300, -50, 24, 24), 48, 72)
        self.time = randint(5, 220) #값을 줄이면 시간간격이 더 빨라짐. 

class Alien(Drawable):
    """ 외계인 객체 """
    def __init__(self, rect, offset, score):
        super().__init__(rect, offset, offset+24)
        self.score = score

def main():
    """ 메인 루틴 """
    sysfont = pygame.font.SysFont(None, 72)
    scorefont = pygame.font.SysFont(None, 36)
    message_clear = sysfont.render("!!CLEARED!!", True, (0, 255, 225))
    message_over = sysfont.render("GAME OVER!!", True, (0, 255, 225))
    message_rect = message_clear.get_rect()
    message_rect.center = (300, 300)
    game_over = False
    moving_left = True
    moving_down = False
    move_interval = 20
    counter = 0
    score = 0
    HP = 100
    aliens = []
    bombs = []
    ship = Ship()
    #beam = Beam()
    beams = [] #빔 배열

    # 외계인 나열과 초기화
    for ypos in range(4): #세로 외계인 4줄
        offset = 96 if ypos < 2 else 144
        for xpos in range(10): #가로 외계인 한줄당 10개
            rect = Rect(xpos*50 + 100, ypos*50 + 50, 24, 24) #간격50
            alien = Alien(rect, offset, (4-ypos)*10) #외계인 득점 40~10점 
            aliens.append(alien)
            #ypos = 0 -> 40점 ypos = 1 -> 30점 (빨강이)
            #ypos 2,3 -> 노랑이

    # 폭탄을 설정
    for _ in range(30): #폭탄은 최대 30?
        beams.append(Bomb())

    space_down = False;

    while True:
        ship_move_x = 0
        ship_move_y = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    ship_move_x = -5
                elif event.key == K_RIGHT:
                    ship_move_x = +5
                elif event.key == K_UP:
                    ship_move_y = -5
                elif event.key == K_DOWN:
                    ship_move_y = +5
                elif event.key == K_SPACE and space_down == False:
                    space_down = True;
                    beams.append(Beam())
                    beams[len(beams)-1].rect.center = ship.rect.center
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    space_down = False;

        if not game_over:
            counter += 1 #외계인의 이동을 위한 카운터
            # 내 캐릭터를 이동
            ship.move(ship_move_x, ship_move_y) #우주선을 이동

            # 빔을 이동
        for beam in beams:
            beam.move(0, -15) #미사일 이동 값을 크게하면 더 빨리 발사.
            if beam.rect.bottom<0:
                beams.remove(beam)
            # 외계인을 이동
            area = aliens[0].rect.copy()
            for alien in aliens:
                area.union_ip(alien.rect) #큰 사각형을 그려 그 안에 있는 외계인이동 시키게 설정.'''

            if counter % move_interval == 0: #외계인이 이동하는 시간 간격 확인
                move_x = -5 if moving_left else 5 #이동 방향에 따라서 x축 이동
                move_y = 0

                #왼쪽벽 또는 오른쪽 벽에 근접하고 아래로 움직이고 있지 않는 경우 
                if (area.left < 10 or area.right > 590) and not moving_down:
                    moving_left = not moving_left #방향을 반대로 변경 --> 벽에 부딪히면 방향전환
                    move_x, move_y = 0, 24 #아래방향으로 24 만큼 이동 --> 방향 전환을 하면 플레이어 쪽으로 이동
                    move_interval = max(1, move_interval - 2) #이동 시간 간격을 줄임 --> 벽에 부딪히면 더 빨라짐.
                    moving_down = True # 현재 아래로 이동중인 상태
                else:
                    moving_down = False #한번 아래로 이동한 후에는 이동 금지

                for alien in aliens:
                    alien.move(move_x, move_y)# 현재 설정값대로 외계인 이동시킴   

            if area.bottom > 550: #외계인 영역이 바닥에 도달했는지 확인
                game_over = True

            # 폭탄을 이동
            for bomb in bombs:
                if bomb.time < counter and bomb.rect.top < 0: #폭탄낙하 준비 확인
                    enemy = aliens[randint(0, len(aliens) - 1)] #폭탄낙하 외계인 선택
                    bomb.rect.center = enemy.rect.center #선택된 외계인에서 폭탄 낙하

                if bomb.rect.top > 0: #폭탄이 낙하중인지 체크함
                    bomb.move(0, 10) #폭탄을 아래 방향으로 10만큼 이동함

                if bomb.rect.top > 600: #폭탄이 화면 바닥까지 낙하했는지 확인
                    bomb.time += randint(50, 250)#다음 폭탄 낙하 시간을 설정함
                    bomb.rect.top = -50 #폭탄을 화면 밖에 위치시키고 낙하 대기

                if bomb.rect.colliderect(ship.rect): #폭탄과 우주선이 충돌하면 게임오버 -10 HP
                    HP -= 10
                    bombs.remove(bomb)
                    if HP == 0:
                        game_over = True

            # 빔과 외계인 충돌?
        for beam in beams: #for 문장으로 바꾸기
            tmp = [] #살아남은 외계인 tmp리스트
            for alien in aliens:
                if alien.rect.collidepoint(beam.rect.center): #충돌검사.
                    beam.rect.top = -50 #빔의 좌표를 안보이는 위치로 이동
                    score += alien.score#외계인을 맞춰서 점수 추가됨
                else:
                    tmp.append(alien)#생존한 외계인을 tmp에 추가함
            aliens = tmp #alien에 빔 맞은 외계인 제외한 생존한 외계인 저장 ----> aliens에 저장
            if len(aliens) == 0: #생존한 외계인이 없다면 게임 끝
                game_over = True

        # 그리기
        SURFACE.fill((0, 0, 0))
        for alien in aliens:
            alien.draw()#외계인 그리기
        ship.draw()#우주선 그리기
        for beam in beams: 
            beam.draw()#우주선 발사하는 빔 그리기
        for bomb in bombs:
            bomb.draw()#외계인 폭탄 그리기

        score_str = str(score).zfill(5) #앞에 0을 추가해서 5자리 만들기
        score_image = scorefont.render(score_str, True, (0, 255, 0))
        SURFACE.blit(score_image, (500, 10))

        HP_image = scorefont.render("HP : "+str(HP), #HP추가
                                     True, "green")
        SURFACE.blit(HP_image,(10,10))

        pygame.draw.rect(SURFACE,(255,0,0),(110,10,HP*2,20)) #빨간색 hp 바 
        pygame.draw.rect(SURFACE,(255,255,255),(110,10,200,20),3) #흰색 테두리
        


        if game_over:
            if len(aliens) == 0: #외계인이 모두 사라진 경우 게임 클리어
                SURFACE.blit(message_clear, message_rect.topleft)
            else:               #외계인이 남아있다면 게임 오버
                SURFACE.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()
