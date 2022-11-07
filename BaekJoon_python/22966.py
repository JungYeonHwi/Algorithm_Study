N=int(input())

name = [0] * N
rank = [0] * N

for i in range(N):
    s = input()
    name[i] = s[:len(s)-2]
    rank[i] = int(s[-1])

d = dict(zip(rank, name))

print(d[min(d.keys())])