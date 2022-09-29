store={}

print("*** 물품과 재고량 입력 ***")
while True:
    item=input("입력 물품==>")
    if item=="z":
        break

    count=int(input("재고량==>"))
    store[item]=count

print("*** 물품의 재고량 확인 ***")

while True:
    item=input("찾을 물품==>")
    if item=="":
        break
    if item in store:#in-검사
        print(store[item],"개 남았어요")
    else:
        print("그 물품은 없습니다")
