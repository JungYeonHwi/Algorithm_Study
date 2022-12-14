x = 1000 - int(input())

cnt = 0

while (x != 0) : 
    if x >= 500 : 
        cnt += 1
        x -= 500
    elif x < 500 and x >= 100 : 
        cnt += 1
        x -= 100
    elif x < 100 and x >= 50 : 
        cnt += 1
        x -= 50
    elif x < 50 and x >= 10 : 
        cnt += 1
        x -= 10
    elif x < 10 and x >= 5 : 
        cnt += 1
        x -= 5
    elif x < 5 : 
        cnt += 1
        x -= 1
        
print(cnt)