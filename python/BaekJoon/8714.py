n = int(input())

arr = list(map(int, input().split()))

if n - sum(arr) > n // 2 : answer = sum(arr)
else : answer = n - sum(arr)

print(answer)