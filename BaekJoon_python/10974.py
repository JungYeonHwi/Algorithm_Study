# 메모리 초과
from itertools import permutations

n = int(input())

data = []

for i in range(1, n+1) : 
    data.append(i)
    
result = list(permutations(data, n))

for i in range(0, len(result)) : 
    one = []
    for j in result[i] : 
        one.append(j)
        
    for key in one : 
        print(key, end=" ")
    print()