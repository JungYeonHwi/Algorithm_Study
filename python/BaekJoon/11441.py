import sys
input = sys.stdin.readline

N = int(input())

A = []
A =list(map(int, input().split()))

answer = [0]*(N+1)

for k in range(N) :
    answer[k] = answer[k-1] + A[k]

M = int(input())

for k in range(M) :
    i, j = map(int, input().split())

    result = answer[j-1]-answer[i-2] 
    print(result)