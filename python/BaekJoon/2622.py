import sys
input = sys.stdin.readline

t = int(input())
answer = 0

for i in range(1, t) : 
    for j in range(i, t) : 
        value = t - i - j
        
        if j > value : break
        if i + j > value : answer += 1
        
        
print(answer)