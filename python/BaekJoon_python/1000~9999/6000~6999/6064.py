import sys

def calculate(m, n, x, y) :
    k = x
    while k <= m * n :
        if (k - x) % m == 0 and (k - y) % n == 0 : 
            return k
        k += m
    return -1

t = int(input())

for _ in range(t) : 
    M, N, x, y = map(int, input().split())
    
    print(calculate(M, N, x, y))