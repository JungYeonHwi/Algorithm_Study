K, N = map(int, input().split())

if N == 1 : print(-1)
else : 
    tmp = (K * N) // (N - 1)
    
    if (K * N) % (N - 1) : tmp += 1
    print(tmp)