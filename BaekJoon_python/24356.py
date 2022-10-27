a, b, c, d = map(int, input().split())

if (a * 60 + b) > (c * 60 + d) : c = c + 24

t = (c * 60 + d) - (a * 60 + b)

print(t, t//30)