import sys

T = int(input())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    books = [False] * (N+1)
    req = []

    for _ in range(M):
        req.append(list(map(int, sys.stdin.readline().split())))
    req.sort(key=lambda x: x[1])

    cnt = 0

    for a, b in req:
        for i in range(a, b+1):
            if not books[i]:
                cnt += 1
                books[i] = True
                break

    print(cnt)