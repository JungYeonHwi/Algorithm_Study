K, N, M = map(int, input().split())

S = K * N

if (M - S < 0) : print(S - M)
else : print(0)