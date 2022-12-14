from itertools import permutations, combinations

n, m = map(int, input().split())
k = sorted(list(map(int, input().split())))
P = sorted(combinations(k, m))

for p in P :
    for i in p :
        print(i, end=' ')
    print('')