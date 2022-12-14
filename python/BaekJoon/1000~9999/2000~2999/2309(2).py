from itertools import combinations

data = []

for i in range(9) : 
    n = int(input())
    data.append(n)
    
result = list(combinations(data, 7))

answer = []

for i in result : 
    if (sum(i) == 100) : answer=i

result = []

for i in answer : 
    result.append(i)
    
result.sort()
for i in result : 
    print(i)