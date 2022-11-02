import math

n, k = map(int, input().split())

num = math.factorial(n)
knum = math.factorial(k)
kknum = math.factorial(n-k)

print(num // (knum * kknum))