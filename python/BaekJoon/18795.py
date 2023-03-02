from sys import stdin

N, M = map(int, stdin.readline().split())
A = map(int, stdin.readline().split())
B = map(int, stdin.readline().split())

sa = sum(A)
sb = sum(B)

print(sa + sb)
