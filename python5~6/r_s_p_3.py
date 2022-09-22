import random

dic={'가위':0,'바위':1,'보':2}

while True:
    user_rsp=input("가위/바위/보 중 입력하시오.")
    rsp=random.choice(["가위","바위","보"])
    print("컴퓨터의 가위/바위/보 ==>",rsp)

    if user_rsp==rsp:
        print("비겼습니다.")
    elif (rsp+1)%3:
        print("이겼습니다")
    else:
        print("졌습니다")
