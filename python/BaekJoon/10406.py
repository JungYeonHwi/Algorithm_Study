w, n, p = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for h in arr :
    if w <= h <= n :
        cnt += 1
print(cnt)