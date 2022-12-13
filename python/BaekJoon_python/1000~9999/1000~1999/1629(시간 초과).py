import sys

A, B, C = map(int, sys.stdin.readline().split())
num = 1

for _ in range(B) : 
    num *= A

print(num % C)