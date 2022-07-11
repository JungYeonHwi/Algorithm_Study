n, m, k = map(int, input().split())

m = m - 1
k -= 3

while (k < 0) : k += n
print((m+k) % n + 1)