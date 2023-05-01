import sys

N, M, K = map(int, sys.stdin.readline().split())

cs = {}
for i in range(N):
    cs[i+1] = 0

for i in range(M):
    genre = list(map(float, sys.stdin.readline().split()))
    for j in range(0, 2*N, 2):
        if genre[j+1] > cs[genre[j]]:
            cs[genre[j]] = genre[j+1]

score = sorted(list(cs.values()), reverse=True)
sum = sum(score[:K])
print('%.1f' % sum)