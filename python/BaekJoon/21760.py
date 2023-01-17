for _ in range(int(input())):
    n, m, k, d = map(int, input().split())
    b = 2*d//(k*n*m*(m-1) + m*m*n*(n-1))
    if b : print(m*(m-1)*n*k*b//2 + m*m*n*(n-1)*b//2)
    else : print(-1)