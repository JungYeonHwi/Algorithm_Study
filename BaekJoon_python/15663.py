from itertools import permutations, combinations, product, combinations_with_replacement

n, m = map(int, input().split())
k = sorted(list(map(int, input().split())))

P = sorted(permutations(k, m))
answer = []
for p in P :
    answer.append(p)
    
answer = sorted(list(set(answer)))

for i in answer : 
    for j in i :
        print(j, end = " ")
    print()