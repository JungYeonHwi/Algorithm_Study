for _ in range(int(input())) : 
    a, b = map(str, input().split())
    
    A = list(a)
    B = list(b)
    
    A.sort()
    B.sort()
    
    if A == B : print("Possible")
    else : print("Impossible")