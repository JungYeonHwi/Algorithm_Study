inf = 9999999999

answer = inf

for i in range(int(input())) : 
    x, y = map(int, input().split())
    
    if x <= y : answer = min(answer, y)
    
if answer == inf : print(-1)
else : print(answer)