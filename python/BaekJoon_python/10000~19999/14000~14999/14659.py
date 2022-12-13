n = int(input())
hills = list(map(int, input().split()))

answer = 0
maxHill = 0
cnt = 0

for i in hills : 
    if i > maxHill : 
        maxHill = i
        cnt = 0
    else : 
        cnt += 1
    answer = max(answer, cnt)
    
print(answer)