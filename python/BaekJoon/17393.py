import sys
input = sys.stdin.readline
from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = []
for idx, a in enumerate(A) :
    answer.append(bisect_right(B, a) - idx - 1)
print(*answer)