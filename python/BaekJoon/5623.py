N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
if N == 2:
    print(1, 1)
else:
    res = [(arr[0][1] + arr[0][2]-arr[1][2])//2]
    for i in range(1, N):
        res.append(arr[0][i]-res[0])
    print(*res)