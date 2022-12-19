from itertools import combinations

n = int(input())
data = list(map(int, input().split()))

result = []

for idx in range(1, n+1) : 
    result.append(list(combinations(data, idx)))
    
cnt = 0
    
for i in result : 
    for j in i : 
        value = list(j)
        s = 0
        for k in value : 
            s += 1/k
        
        if s >= 0.99 and s <= 1.01 : cnt += 1

print(cnt)