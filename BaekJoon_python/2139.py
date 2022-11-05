import datetime

while 1 : 
    day, month, year = map(int, input().split())
    
    if day == 0 and month == 0 and year == 0 : break
    inputDay = datetime.datetime(year, month, day)
    stdDay = datetime.datetime(year, month = 1, day = 1)
    
    info = inputDay - stdDay
    
    print(info.days + 1)