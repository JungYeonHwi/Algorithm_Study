from itertools import permutations

n = int(input())
k = int(input())
data = [input().rstrip() for _ in range(n)]
    
answer = set()

for per in permutations(data, k) : 
    answer.add("".join(per))
    
print(len(answer))