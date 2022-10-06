secureFile=None
inStr,secure="",""

secureFile=open("C:/Users/user/Desktop/python0/secure.txt","w",encoding="UTF-8")

while True:
    inStr=input('스파이에게 전달할 메시지==>')
    if inStr=="":
        break
    for ch in inStr:
        num=ord(ch)
        num+=100
        secure+=chr(num)

secureFile.writelines(secure)
secureFile.close()
print("======secure.txt 암호화 완료======")
