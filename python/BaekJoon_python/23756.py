n = int(input())
start = int(input())
answer = 0

for i in range(n):
    go = int(input())
    answer += min(abs(start - go), 360 - start + go, start + 360 - go)
    start = go
print(answer)
