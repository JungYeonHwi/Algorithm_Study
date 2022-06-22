from itertools import permutations

n, m = map(int, input().split())

items = []

for i in range(1, n+1) : 
    items.append(i)

result = permutations(items, m)

for i in result : 
    print(' '.join(map(str, i)))
