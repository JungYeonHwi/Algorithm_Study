from itertools import permutations

n = int(input())

data = list(map(int, input().split()))
    
result = list(permutations(data, n))
answer = []

for i in range(0, len(result)) : 
    one = []
    for j in result[i] : 
        one.append(j)
        
    s = []
    for j in range(0, len(one)-1) : 
        s.append(abs(one[j] - one[j+1]))
        
    answer.append(sum(s))
    
print(max(answer))