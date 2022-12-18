import random

class Object:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 이(가) 생성 되었습니다.')
        print(f'체력 : {self.hp}, 물리 공격력 : {self.damage}')

    def attack(self,target):
        print(f'{self.name}가 {target.name}을 {self.damage}의 물리 공격력으로 공격했습니다.')
        target.hp -= self.damage
        return target.hp



class TeamA_Player(Object):
    def __init__(self,name,hp,damage):
        Object.__init__(self,name,hp,damage)

class TeamB_Player(Object):
    def __init__(self,name,hp,damage):
        Object.__init__(self,name,hp,damage)

def TeamA_Player_action():
    print("1.워리어 공격")
    print("2.마법사 공격")
    print("3.궁수 공격")
    player_behavior = int(input("공격할려면 1,2,3번 중 입력"))

    print("대상 선택 -->")
    print("1.전사")
    print("2.마법사")
    print("3.궁수")
    player_num = int(input("공격 할 대상의 번호를 입력하시오."))
    if TeamA_p1 in TeamA_list:
        if player_behavior == 1:
            if player_num == 1:
                TeamB_p1.hp = TeamA_p1.attack
            elif player_num == 2:
                TeamB_p2.hp = TeamA_p1.attack
            elif player_num == 3:
                TeamA_p3.hp = TeamA_p1.attack


    if TeamA_p2 in TeamA_list:
        if player_behavior == 2:
            if player_num == 1:
                TeamB_p1.hp = TeamA_p2.attack
            elif player_num == 2:
                TeamB_p2.hp = TeamA_p2.attack
            elif player_num == 3:
                TeamA_p3.hp = TeamA_p2.attack


    if TeamA_p3 in TeamA_list:
        if player_behavior == 3:
            if player_num == 1:
                TeamB_p1.hp = TeamA_p3.attack
            elif player_num == 2:
                TeamB_p2.hp = TeamA_p3.attack
            elif player_num == 3:
                TeamB_p3.hp = TeamA_p3.attack


def TeamB_Player_action():
    print("1.워리어 공격")
    print("2.마법사 공격")
    print("3.궁수 공격")
    player_behavior = int(input("공격할려면 1,2,3번중 입력"))

    print("대상 선택 -->")
    print("1.전사")
    print("2.마법사")
    print("3.궁수")
    player_num = int(input("공격 할 대상의 번호를 입력하시오."))

    if TeamB_p1 in TeamB_list:
        if player_behavior == 1:
            if player_num == 1:
                TeamA_p1.hp = TeamB_p1.attack
            elif player_num == 2:
                TeamA_p2.hp = TeamB_p1.attack
            elif player_num == 3:
                TeamA_p3.hp = TeamB_p1.attack

    if TeamB_p2 in TeamB_list:
        if player_behavior == 1:
            if player_num == 1:
                TeamA_p1.hp = TeamB_p2.attack
            elif player_num == 2:
                TeamA_p2.hp = TeamB_p2.attack
            elif player_num == 3:
                TeamA_p3.hp = TeamB_p2.attack


    if TeamB_p3 in TeamB_list:
        if player_behavior == 1:
            if player_num == 1:
                TeamA_p1.hp = TeamB_p3.attack
            elif player_num == 2:
                TeamA_p2.hp = TeamB_p3.attack
            elif player_num == 3:
                TeamA_p3.hp = TeamB_p3.attack


def TeamA_death():
    if TeamA_p1.hp <= 0 :
        if TeamA_p1 in TeamA_list:
            TeamA_list.remove(TeamA_p1)

    if TeamA_p2.hp <= 0 :
        if TeamA_p2 in TeamA_list:
            TeamA_list.remove(TeamA_p2)

    if TeamA_p3.hp <= 0 :
        if TeamA_p3 in TeamA_list:
            TeamA_list.remove(TeamA_p3)

def TeamB_death():
    if TeamB_p1.hp <= 0 :
        if TeamB_p1 in TeamB_list:
            TeamB_list.remove(TeamB_p1)

    if TeamB_p2.hp <= 0 :
        if TeamB_p2 in TeamB_list:
            TeamB_list.remove(TeamB_p2)

    if TeamB_p3.hp <= 0 :
        if TeamB_p3 in TeamB_list:
            TeamB_list.remove(TeamB_p3)

TeamA_p1 = TeamA_Player("워리어", 100,random.randint(5,10))
TeamA_p2 = TeamA_Player("마법사", 80,random.randint(7,12))
TeamA_p3 = TeamA_Player("궁수", 60,random.randint(4,20))

TeamB_p1 = TeamB_Player("워리어", 100,random.randint(5,10))
TeamB_p2 = TeamB_Player("마법사", 80,random.randint(7,12))
TeamB_p3 = TeamB_Player("궁수", 60,random.randint(4,20))

TeamA_list = [TeamA_p1,TeamA_p2,TeamA_p3]
TeamB_list = [TeamB_p1,TeamB_p2,TeamB_p3]

turn = 0

while True:
    print("=== 턴 시작전 총 턴 표시 ===")

    if turn % 2 == 0:
        print("TeamA의 플레이 턴 ")

        TeamA_Player_action()

        if len(TeamB_list) <= 0:
            print("이겼습니다.")
            break


    else:
        print("TeamB의 플레이 턴")

        TeamB_Player_action()

        if len(TeamA_list) <= 0:
            print("이겼습니다.")

    turn += 1
    print("--------------")
    print("턴 종료")
    print("--------------")