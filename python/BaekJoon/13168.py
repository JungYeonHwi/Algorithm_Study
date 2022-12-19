import sys
input = sys.stdin.readline

from math import inf

N, R = map(int, input().split())
cities = set(input().split())
N = len(cities)
ctoi = {city: i for i, city in enumerate(cities)}
M = int(input())
root = list(map(lambda x: ctoi[x], input().split()))

normal = [[inf] * N for _ in range(N)]
railro = [[inf] * N for _ in range(N)]

for _ in range(int(input())):
    t, s, e, c = input().split()
    s = ctoi[s]
    e = ctoi[e]
    c = int(c)
    if normal[s][e] > c :
        normal[s][e] = c
        normal[e][s] = c
    if t in ['Mugunghwa', 'ITX-Saemaeul', 'ITX-Cheongchun'] :
        railro[s][e] = 0
        railro[e][s] = 0
    elif t in ['S-Train', 'V-Train'] :
        if railro[s][e] > c / 2 :
            railro[s][e] = c / 2
            railro[e][s] = c / 2
    else :
        if railro[s][e] > c :
            railro[s][e] = c
            railro[e][s] = c

for k in range(N) :
    normal[k][k] = 0
    railro[k][k] = 0
    for i in range(N):
        for j in range(N) :
            normal[i][j] = min(normal[i][j], normal[i][k] + normal[k][j])
            railro[i][j] = min(railro[i][j], railro[i][k] + railro[k][j])

normalCost = railroCost = 0
for i in range(M - 1):
    normalCost += normal[root[i]][root[i + 1]]
    railroCost += railro[root[i]][root[i + 1]]

print('Yes') if railroCost + R < normalCost else print('No')