L, R, A = map(int, input().split())
a, b = min(L, R), max(L, R)
t = min(A, b-a)

a += t
A -= t

if A : res = a * 2 + (A // 2 * 2)
else : res = a * 2
print(res)