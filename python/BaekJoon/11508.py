import sys
input = sys.stdin.readline

n = int(input())
c =[]
for i in range(n) :
  c.append(int(input()))
c.sort(reverse=True)

result = 0
for i in range(2, len(c), 3) :
  result += c[i]

print(sum(c) - result)