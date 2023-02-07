n, m = map(int, input().split())
pay = list(map(int, input().split()))
result = pay + [0] * m

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n + m):
        result[i] -= arr[j]
        result[j] += arr[j]
print(*result)