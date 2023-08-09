k = int(input())
a, b, c, d = list(map(int, input().split()))

r1 = a*k + b
r2 = c*k + d

if r1 == r2:
    print("Yes",r1)
else:
    print("No")
