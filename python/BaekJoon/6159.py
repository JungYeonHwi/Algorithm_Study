from sys import stdin

n, s = map(int, stdin.readline().split())

cs = []

pc = 0

for i in range(n) : 
  v = int(stdin.readline())
  cs.append(v)

for c1 in range(n-1) :
  for c2 in range(c1 + 1, n) :
    if cs[c1] + cs[c2] <= s : pc += 1


print(pc)
