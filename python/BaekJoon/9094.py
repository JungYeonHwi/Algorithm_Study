import sys
input = sys.stdin.readline

maxValue = 101
table = [[0] * maxValue for _ in range(maxValue)]
for a in range(1, maxValue-1):
    for m in range(1, maxValue):
        table[a][m] = table[a-1][m]
        for b in range(1, a):
            if not (a*a+b*b+m) % (a*b):
                table[a][m] += 1


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(str(table[N-1][M]))
