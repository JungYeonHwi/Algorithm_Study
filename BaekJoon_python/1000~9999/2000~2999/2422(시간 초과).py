import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())
ice = [i for i in range(1, n+1)]
result = list(combinations(ice, 3))
cnt = 0

no = []

for _ in range(m) : 
    a, b = map(int, input().split())
    no.append([a, b])
    
for i in result : 
    value = list(i)
    
    for j in no : 
        a = j[0]
        b = j[1]
        
        if a in value and b in value : 
            cnt += 1
            break
        
print(len(result) - cnt)