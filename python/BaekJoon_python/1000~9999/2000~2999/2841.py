import sys

N, P = map(int, input().split())
cnt = 0
arr = [[] for _ in range(7)]

for i in range(N) :
    n, p = map(int, sys.stdin.readline().split())
    if not arr[n-1] :
        arr[n-1].append(p)
        cnt += 1
    else :
        while arr[n-1] and p < arr[n-1][-1] :
            arr[n-1].pop()
            cnt += 1
        if not arr[n-1] or p > arr[n-1][-1] :
            arr[n-1].append(p)
            cnt += 1
        else :
            pass
print(cnt)
