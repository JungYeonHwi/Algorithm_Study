import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
goal = [1, m + 1]	
record = []

for i in range(k):
    cl = list(map(int, input().split()))
    record.append(abs(goal[0] - cl[0]) + abs(goal[1] - cl[1]))

print(record.index(min(record)) + 1)	