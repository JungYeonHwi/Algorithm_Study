import sys
input = sys.stdin.readline

value = lambda: map(int, input().strip().split())

N = int(input())
chapters = list(int(input()) for _ in range(N))

ans = 0
cnt = 0

if N == 1:
    pass

while cnt < N:
    left = 30
    while left > 0:
        if (left > chapters[cnt]):
            ans += 1
            left -= chapters[cnt]
            cnt += 1

            if cnt >= N : break

        elif left * 2 >= chapters[cnt] : 
            ans += 1
            cnt += 1
            break

        elif chapters[cnt] > left * 2 :
            cnt += 1
            break

print(ans)