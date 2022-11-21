n = int(input())
arr = []
answer = []

for _ in range(n) : 
    arr.append(int(input()))
    
arr.sort(reverse=True)    
    
for i in range(n) : 
    tips = arr[i] - (i+1 - 1)
    
    if tips >= 0 : answer.append(tips)
    
print(sum(answer))