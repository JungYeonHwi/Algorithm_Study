from datetime import datetime

def check(s):
    answer = 0
    
    for year in range(s, s + 1000) :
        if year % 400 == 0 : answer += 366
        elif year % 100 == 0 : answer += 365
        elif year % 4 == 0 : answer += 366
        else : answer += 365
            
    return answer

def DDAY(today, dday):
    todayDate = datetime(year=today[0], month=today[1], day=today[2])
    ddayDate = datetime(year=dday[0], month=dday[1], day=dday[2])
    
    ddayDay = (ddayDate - todayDate).days
    
    year1000 = check(today[0])
    
    if ddayDay >= year1000 : ddayDay = "gg"
    else : ddayDay = f"D-{ddayDay}"
    
    return ddayDay

today = list(map(int, input().split()))
dday = list(map(int, input().split()))

answer = DDAY(today, dday)
print(answer)