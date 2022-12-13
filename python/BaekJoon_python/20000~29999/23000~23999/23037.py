import sys
input = sys.stdin.readline

n = input().rstrip()

s = 0

for i in range(len(n)) : 
    tmp = int(n[i])
    s += tmp ** 5
    
print(s)