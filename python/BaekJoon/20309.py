N = int(input())
arr = list(map(int, input().split()))
ok = 1
for i in range(N):
    if i % 2 :
        if arr[i] % 2 :
            ok = 0
print("YES" if ok else "NO")