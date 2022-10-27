num1, num2 = map(int, input().split())

a, b = 100 - num1, 100 - num2
c = 100 - (a + b)
d = a * b
q, r = d // 100, d % 100

print(a, b, c, d, q, r)
print(c + q, r)