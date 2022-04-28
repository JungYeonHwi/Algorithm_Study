N = int(input())
cnt = 0
m = 0
for _ in range(N):
    name = input()
    K, M = map(int, input().split())
    evol = 0
    while K <= M:
        M -= K
        M += 2
        evol += 1
    cnt += evol
    if evol > m:
        m = evol
        mname = name

print(cnt)
print(mname)