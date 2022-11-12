import sys
input = sys.stdin.readline

A, B = map(int, input().split())

C, D = A // B, A % B
if A != 0 and D < 0 :
    C, D = C + 1, D - B
print(C)
print(D)