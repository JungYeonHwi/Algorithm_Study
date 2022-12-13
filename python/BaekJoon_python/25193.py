import math

n = int(input())
arr = list(map(str, input()))
cnt = 0

for i in arr : 
    if i == "C" : 
        cnt += 1
        
if cnt % (n+1) == 0 : print(cnt//(n-cnt))
else : print(math.ceil(cnt/(n-cnt+1)))