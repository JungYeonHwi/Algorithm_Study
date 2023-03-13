n = int(input())
data = []
for _ in range(n) :
      data.append(int(input()))
data.sort()

v = 1000001
for i in range(n // 2) :
  value = data[i] + data[-(i+1)]
  v = min(v, value)

print(v)