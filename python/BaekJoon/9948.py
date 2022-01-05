from datetime import datetime

def convert(strMonth):
    dict = { "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11,"December": 12 }
    
    return dict[strMonth]


def getDay(birthday):
    day, month = birthday.split()
    
    day = int(day)
    
    month = convert(strMonth=month)
    
    return day, month

arr = []

while 1 :
    birthday = input()
    
    if birthday == "0 #" : break
        
    arr.append(birthday)
    
    
for birthday in arr :
    day, month = getDay(birthday=birthday)
    
    if day == 29 and month == 2 : answer = "Unlucky"
    elif day == 4 and month == 8 : answer = "Happy birthday"
    else :    
        bd = datetime(year=2007, month=month, day=day)
        sd = datetime(year=2007, month=8, day=4)
        
        if bd < sd : answer = "Yes"
        else :answer = "No"
            
    print(answer)