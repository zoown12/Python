secureFile=None
inStr,decode="",""

secureFile=open("C:/Users/user/Desktop/python0/secure.txt","r",encoding="UTF-8")

inStr=secureFile.readline()
for ch in inStr:
    num=ord(ch)
    num-=100
    decode+=chr(num)

secureFile.close()
print('암호 해독 결과',decode)
