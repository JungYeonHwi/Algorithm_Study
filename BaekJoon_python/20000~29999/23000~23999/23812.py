n = int(input())
s = '@' * n
midS = '@' * n + ' ' * n * 3 + '@' * n

for i in range(n) : print(midS)
for i in range(n) : print(s*5)
for i in range(n) : print(midS)
for i in range(n) : print(s*5)
for i in range(n) : print(midS)