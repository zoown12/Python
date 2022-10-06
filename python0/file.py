inFile = None
inStr=""


inFile=open("C:/Users/user/Desktop/python0/pt01.txt","r",encoding="UTF-8")
while True:
    inStr=inFile.readline()
    if inStr=="":
        break
    print(inStr,end='')

inFile.close()
