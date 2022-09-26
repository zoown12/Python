import random
for i in range(1,6,1):
    user_num=int(input("guess the number"))
    com_num=random.randint(1,100)
    print(i,"번째 시도")
    if(user_num == com_num):
        print("정답입니다")
        break
    elif(user_num<com_num):
        print("예상보다 숫자가 더 큽니다.")
        continue
    elif(user_num>com_num):
        print("예상보다 숫자가 더 작습니다")
        continue
    elif(i==6):
        print("게임 종료, 정답은",con_num,"입니다")
        break
                
