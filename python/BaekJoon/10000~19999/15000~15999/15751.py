a, b, c, d = map(int, input().split())
A = max(a, b)
B = min(a, b)
C = max(c, d)
D = min(c, d)

dist1 = A - B
dist2 = abs(A - C) + abs(B - D)
print(min(dist1, dist2))