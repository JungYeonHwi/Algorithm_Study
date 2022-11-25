import sys
input = sys.stdin.readline

k = int(input())
s = input()

print(s[0], end="")

for i in range(k, len(s), k) : 
    print(s[i], end="")