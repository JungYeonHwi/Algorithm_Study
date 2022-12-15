import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
    
data = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())

    for j in range(a, b):
        data[j] = 1

answer = n - data.count(1)

print(answer)