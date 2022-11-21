from itertools import permutations

n, k = map(int, input().split())
data = []

for _ in range(n) : 
    data.append(int(input()))

result = list(permutations(data, n))
answer = len(result)

for per in result : 
    one = []
    for i in per : 
        one.append(i)
    
    for i in range(len(one)-1) : 
        a = one[i]
        b = one[i+1]
        
        if abs(a-b) <= k : 
            answer -= 1
            break

print(answer)
