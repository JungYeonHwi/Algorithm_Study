for _ in range(int(input())) : 
    n = int(input())
    nn = n * n
    nn = str(nn)
    start = -1 * len(str(n))
    
    value = int(nn[start:])
    
    if value == n : print("YES")
    else : print("NO")