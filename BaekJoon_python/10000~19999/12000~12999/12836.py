import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
money = [0] * (N + 1)

for _ in range(Q) :
    query, p, q = map(int, input().split())
    if query == 1 : money[p] += q
    else : print(sum(money[p:q + 1]))