R, C, N = map(int, input().split())

if R%N : a = R // N + 1
else : a = R // N
if C%N : b = C//N + 1
else : b = C // N

print(a * b)