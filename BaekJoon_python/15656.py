from itertools import permutations, combinations, product

n, m = map(int, input().split())
k = sorted(list(map(int, input().split())))

P = sorted(product(k, repeat=m))

for p in P :
    for i in p :
        print(i, end=' ')
    print('')