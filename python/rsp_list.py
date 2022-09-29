import random
toss=[]

for i in range(10000):
    comA=random.choice(["가위","바위","보"])
    comB=random.choice(["가위","바위","보"])
    if comA==comB:
        toss.append("없음")
    elif comA=="가위":
        if comB=="바위":
            toss.append("B")
        elif comB=="보":
            toss.append("A")
    elif comA=="바위":
        if comB=="보":
            toss.append("B")
        elif comB=="가위":
            toss.append("A")
    elif comA=="보":
        if comB=="가위":
            toss.append("B")
        elif comB=="바위":
            toss.append("A")
awin=toss.count("A")
bwin=toss.count("B")
draw=toss.count("없음")

print("A가 이긴횟수:",awin)
print("b가 이긴횟수:",bwin)
print("비긴횟수:",draw)
