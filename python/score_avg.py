print("홍길동 선수 경기 끝났습니다")
score_list=[]
for i in range(5):
    jumsu=int(input("평가 점수===>"))
    score_list.append(jumsu)

hap=0
for i in range(5):
    hap+=score_list[i]

avg=hap/len(score_list)
print("심사평균 점수 :",avg)
