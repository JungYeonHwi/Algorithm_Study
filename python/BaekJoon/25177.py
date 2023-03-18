N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if N < M : a += [0] * (M-N)

answer = 0
for i in range(M) :
    answer = max(answer, b[i] - a[i])

print(answer)