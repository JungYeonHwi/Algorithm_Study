N = int(input())
cnt = 0

while N != 0:
    if N % 2 == 1:
        cnt += 1
    N //= 2
print(cnt)