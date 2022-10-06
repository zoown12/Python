inFile = None
inList=[]

inFile=open("C:/Users/user/Desktop/python0/pt01.txt","r",encoding="UTF-8")
inList=inFile.readlines()
print(inList,end='')

inFile.close()
