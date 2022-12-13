a, b = input().split()
m = int(a.replace('6', '5')) + int(b.replace('6', '5'))
M = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(m, M)