N = int(input())
result = 1
for i in range(2, N+1):
    result *= i

print(int(result / 60 / 60 / 24 / 7))
