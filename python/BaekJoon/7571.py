N, M = map(int, input().split())
X, Y = [], []
for _ in range(M) :
    i, j = map(int, input().split())
    X.append(i)
    Y.append(j)
X.sort()
Y.sort()

x, y = X[M//2], Y[M//2]
res = 0

for i in range(M) :
    res += abs(x-X[i]) + abs(y-Y[i])
print(res)