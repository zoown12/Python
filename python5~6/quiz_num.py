import random
num=0
for i in range(1,11,1):
    num_user=int(input("숫자를 입력하시오."))
    num=random.randint(1,5)
    print("게임",i,"회",end='')

    if num_user==num:
        print("맞혔네요. 축하드립니다!!")
        break
    else:
        print("아까워요!!!",num,"였는데 다시해보세요")
        continue
print("게임을 마칩니다")
    
