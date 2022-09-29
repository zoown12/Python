from datetime import datetime,timedelta

def getCurrent():
    curDate=datetime.now()#현재 날짜 및 시간을 구함
    return curDate
def getAfterDate(now,day):
    retDate=now+timedelta(days=day)#현재에 timedelta를 더해 지난 일자를 구함
    return retDate
nowDate,afterDate=None,None

nowDate=getCurrent()
print("현재 날짜와 시간==>",nowDate)
afterDate=getAfterDate(nowDate,100)
print("100일 후 날짜와 시간==>",afterDate)
