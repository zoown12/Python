inFile,outFile=None,None
inStr=""

inFile=open("C:/Users/user/Desktop/python0/test.txt","r",encoding="UTF-8")
outFile=open("C:/Users/user/Desktop/python0/note.txt","w")

inList=inFile.readlines()
for inStr in inList:
    outFile.writelines(inStr)

inFile.close()
outFile.close()
print("---test.txt가 note.txt로 복사되었음---")
