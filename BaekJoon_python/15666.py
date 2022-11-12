from itertools import permutations, combinations, product, combinations_with_replacement

n, m = map(int, input().split())
k = sorted(list(map(int, input().split())))

ans = list(combinations_with_replacement(k, m))
ans = list(set(ans))
ans.sort()

if m == 1 :
    for t in range(0, len(ans)) :
        s = list(ans[t])
        print(s[0])
else :
    for t in range(0, len(ans)) :
        s = list(ans[t])
        for u in range(0, len(s)-1) :
            print(s[u], end=" ")
            
        print(s[len(s)-1])