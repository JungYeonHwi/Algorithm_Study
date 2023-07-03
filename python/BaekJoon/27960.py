import sys
input = sys.stdin.readline

a, b = map(int, input().split())

binA = bin(a)
binB = bin(b)

res = int(bin(a^b)[2:], 2)
print(res)