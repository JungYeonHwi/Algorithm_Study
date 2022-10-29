a, b = map(int, input().split())
c, d = map(int, input().split())

a1 = int(c)
b1 = int(a)
c1 = int(d)
d1 = int(b)

a2 = int(d)
b2 = int(c)
c2 = int(b)
d2 = int(a)

a3 = int(b)
b3 = int(d)
c3 = int(c)
d3 = int(a)

one = a / c + b / d
two = a1 / c1 + b1 / d1
three = a2 / c2 + b2 / d2
four = a3 / c3 + b3 / d3

arr = [one, two, three, four]

m = max(arr)

idx = arr.index(m)
print(idx)