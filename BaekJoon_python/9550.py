for i in range(int(input())) :
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    for i in arr :
        ans += i//K
    print(ans)