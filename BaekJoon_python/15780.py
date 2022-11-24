N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = sum([(n+1)//2 for n in arr])

print("YES" if cnt >= N else "NO")