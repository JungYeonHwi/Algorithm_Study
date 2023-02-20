n, k, a, b = map(int, input().split())

stair = (n-1) * a
el = (k-1) * b + (n-1) * b

print(el, stair)