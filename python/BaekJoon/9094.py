import sys
input = sys.stdin.readline

_max = 101
table = [[0] * _max for _ in range(_max)]
for a in range(1, _max-1):
    for m in range(1, _max):
        table[a][m] = table[a-1][m]
        for b in range(1, a):
            if not (a*a+b*b+m) % (a*b):
                table[a][m] += 1


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(str(table[N-1][M]))
