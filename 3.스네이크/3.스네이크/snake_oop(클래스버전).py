import sys
import random
import pygame
from pygame.locals import QUIT, \
    KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode([600, 600])
FPSCLOCK = pygame.time.Clock()

class Snake:
    """ Snake 객체 """
    bodies = []
    def __init__(self, pos):
        self.bodies = [pos]

    def move(self, key):
        """ Snake를 1프레임만큼 이동 """
        xpos, ypos = self.bodies[0]
        if key == K_LEFT:
            xpos -= 1
        elif key == K_RIGHT:
            xpos += 1
        elif key == K_UP:
            ypos -= 1
        elif key == K_DOWN:
            ypos += 1
        head = (xpos, ypos)

        # 게임 오버 판정
        is_game_over = head in self.bodies or  \
            head[0] < 0 or head[0] >= W or \
            head[1] < 0 or head[1] >= H

        self.bodies.insert(0, head)
        if head in FOODS:
            # 먹이를 다른 장소로 이동
            i = FOODS.index(head)
            del FOODS[i]
            add_food(self)
        else:
            self.bodies.pop()

        return is_game_over

    def draw(self):
        """ Snake를 그린다 """
        for body in self.bodies:
            pygame.draw.rect(SURFACE, (0, 255, 255),
                             Rect(body[0]*30, body[1]*30, 30, 30))

FOODS = []
(W, H) = (20, 20)

def add_food(snake):
    """ 임의의 장소에 먹이를 배치 """
    while True:
        pos = (random.randint(0, W-1), random.randint(0, H-1))
        if pos in FOODS or pos in snake.bodies:
            continue
        FOODS.append(pos)
        break

def paint(snake, message):
    """ 화면 전체 그리기 """
    SURFACE.fill((0, 0, 0))
    snake.draw()
    for food in FOODS:
        pygame.draw.ellipse(SURFACE, (0, 255, 0),
                            Rect(food[0]*30, food[1]*30, 30, 30))
    for index in range(20):
        pygame.draw.line(SURFACE, (64, 64, 64),
                         (index*30, 0), (index*30, 600))
        pygame.draw.line(SURFACE, (64, 64, 64),
                         (0, index*30), (600, index*30))
    if message != None:
        SURFACE.blit(message, (150, 300))
    pygame.display.update()

def main():
    """ 메인 루틴 """
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False
    snake = Snake((int(W/2), int(H/2)))
    for _ in range(10):
        add_food(snake)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key

        if game_over:
            message = myfont.render("Game Over!", True,
                                    (255, 255, 0))
        else:
            game_over = snake.move(key)

        paint(snake, message)
        FPSCLOCK.tick(5)

if __name__ == '__main__':
    main()
