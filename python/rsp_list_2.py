import random
toss=[]

for i in range(10000):
    comA=random.randint(0,3)
    comB=random.randint(0,3)
    if comA==comB:
        toss.append("없음")
    elif (comA+1) % 3 == comB:
        toss.append("A")
    else:
        toss.append("B")
awin=toss.count("A")
bwin=toss.count("B")
draw=toss.count("없음")

print("A가 이긴횟수:",awin)
print("b가 이긴횟수:",bwin)
print("비긴횟수:",draw)
