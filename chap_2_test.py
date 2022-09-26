#1
sec=int(input("enter sec"))
minute=sec//60
sec_sec=sec%60
print(minute,"분",sec_sec,"초")

#2
minute_2=int(input("enter min"))
hour=minute_2//60
day=hour//24
minute_3=minute_2%60
hour=hour%24
print(day,"일",hour,"시",minute_3,"분")

#3
rate=0.05
year=1
money=int(input("enter money"))
for i in range(1, 6 ,1):
    money=money*(1+rate*year)
    print(money)

#4
sum_1=0
for j in range(1,101,1):
    sum_1+=j
    print(sum_1)

#5
podo=int(input("enter podo"))
berry=int(input("enter berry"))
podo_sum=podo*75
berry_sum=berry*113.5
total=podo_sum+berry_sum
print(podo_sum,berry_sum,total)
