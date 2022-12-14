from itertools import permutations, combinations, product, combinations_with_replacement

n, m = map(int, input().split())
k = sorted(list(map(int, input().split())))

P = sorted(combinations_with_replacement(k, m))

for p in P :
    for i in p :
        print(i, end=' ')
    print('')