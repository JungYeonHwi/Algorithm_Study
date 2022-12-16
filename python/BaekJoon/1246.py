N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(M)])
maxP = maxB = 0
for i in range(M) :
    t = arr[i] * ((M-i) if M-i <= N else N)
    if maxB < t:
        maxB = t
        maxP = arr[i]
print(maxP, maxB)