n, k = map(int, input().split())
num = []
js = 0
bj = 0
for i in range(n):
    num.append(float(input()))
num.sort()
for i in range(k, n-k):
    js += num[i]
bj = js
js /= (n - 2 * k)
bj = bj + (num[k] * k) + (num[n-k-1] * k)
bj /= n
print('%.2f'%(js + 0.00000001))
print('%.2f'%(bj + 0.00000001))