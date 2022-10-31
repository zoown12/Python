days = {'January':31, 'February':28, 'March':31, 'April':30,
'May':31, 'June':30, 'July':31, 'August':31,
'September':30, 'October':31, 'November':30, 'December':31}

user_=input("월을 입력하시오.")
print(days[user_])

print(sorted(days))

for k,v in days.items():
    #print(k,v)
    if(v==31):
        print(k)

its2=[]
for v,k in days.items():
    its2.append((k,v))
print(its2)
      
m=input('월명 3자만 입력하시오.')

for k in days:
    if m in k:
        print(k)
