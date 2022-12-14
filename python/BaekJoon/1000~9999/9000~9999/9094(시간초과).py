import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    count = 0

    for a in range(1, n - 1):
        for b in range(a + 1, n):
            t = a * a + b * b + m
            if t % (a * b) == 0 : count += 1
    print(count)