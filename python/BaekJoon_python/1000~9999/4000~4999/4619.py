while 1 : 
    B, N = map(int, input().split())
    
    if B == 0 and N == 0 : break
    else : 
        i = 0
        while i ** N < B : i += 1
        if i ** N - B < B - (i - 1) ** N : print(i)
        else : print(i-1)