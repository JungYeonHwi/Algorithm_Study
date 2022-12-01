from math import gcd, sqrt
n = int(input())
arr = []

if n == 2:
    a, b = map(int, input().split())
    value = gcd(a, b)


if n == 3:
    a, b, c = map(int, input().split())
    value = gcd(gcd(a, b), c)

for i in range(1, int(sqrt(value)) + 1) :
    if value % i == 0 :
        arr.append(i)
        if i**2 != value :
            arr.append(value // i)

arr.sort()

for num in arr : print(num)