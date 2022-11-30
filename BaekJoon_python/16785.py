A, B, C = map(int, input().split())
cnt = total = 0

while total < C :
    total += A
    cnt += 1
    if cnt%7 == 0 : total += B
print(cnt)