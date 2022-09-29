def cal(v1,v2,op):
    result=0
    if op=='+':
        result=v1+v2
    elif op=='-':
        result=v1-v2
    elif op=='*':
        result=v1*v2
    elif op=='//':
        result=v1//v2
    elif op=='%':
        result=v1%v2
    return result
res=0
var1,var2,oper=0,0,""

oper=input("계산 입력(+,-,*,//,%):")
var1=int(input("enter var1==>"))
var2=int(input("enter var2==>"))
res=cal(var1,var2,oper)
print("##계산기:",var1,oper,var2,"=",res)
