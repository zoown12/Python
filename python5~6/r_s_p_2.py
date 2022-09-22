import random
while True:
    rsp=random.choice(["가위","바위","보"])
    user_rsp=input("가위/바위/보 중 입력하시오.")
    print("컴퓨터의 가위/바위/보 ==>",rsp)
    if user_rsp == rsp:
        print("비겼습니다")
    
    if user_rsp=="가위":
        if rsp=="바위":
            print("졌습니다")
        elif rsp=="보":
            print("이겼습니다")
    
    if user_rsp=="보":
        if rsp=="가위":
            print("졌습니다")
        elif rsp=="바위":
            print("이겼습니다")

    if user_rsp=="바위":
        if rsp=="보":
            print("졌습니다")
        elif rsp=="가":
            print("이겼습니다")
