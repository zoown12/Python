import random

def lotto():
    lottoNum=random.randint(1,45)
    return lottoNum

lottoList=[]

print("** 로또 추첨을 시작합니다. **")
while True:
    num=lotto()

    if num in lottoList:
        continue
    else:
        lottoList.append(num)
    if len(lottoList) == 7:
        break

print("오늘의 로또 번호 ==>",end='')
lottoList.sort()
for i in range(0,6):
    print(lottoList[i]," ",end='')
for i in range(6,7):
    print(lottoList[i]," ",end='')
