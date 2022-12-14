n = int(input())
k = int(input())
x = min(k + 60, n)
answer = x * 1500 + (n - x) * 3000
print(answer)