e, f, c = map(int, input().split())
s = e + f
i = 0

while s >= c:
    i += s // c
    s = s // c + s % c
print(i)