a, b, c = map(int, input().split())

e = 229 * 324 * a * 2
p = 297 * 420 * b * 2
s = 210 * 297 * c

print("{:.6f}".format((e + p + s) * 0.000001))