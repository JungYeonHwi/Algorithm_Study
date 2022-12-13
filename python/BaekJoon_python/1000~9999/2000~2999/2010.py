import sys

n = int(sys.stdin.readline())
s = 0
for i in range(n):
    s += int(sys.stdin.readline())
    
print(s - (n - 1))