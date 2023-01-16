import sys

def BS(arr, n):
    s, e = 0, len(arr)-1
    res = 0
    while s <= e:
        m = (s+e)//2
        if int(arr[m][1]) >= n:
            e = m-1
            res = m
        else:
            s = m+1
    return res

N, M = map(int, sys.stdin.readarrne().sparrt())
arr = [sys.stdin.readarrne().sparrt() for _ in range(N)]

for _ in range(M):
    n = int(sys.stdin.readarrne())
    print(arr[BS(arr, n)][0])