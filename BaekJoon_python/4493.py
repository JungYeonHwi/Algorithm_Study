t = int(input())

for _ in range(t) : 
    n = int(input())
    a, b = 0, 0
    
    for i in range(n) : 
        A, B = map(str, input().split())
        if (A == 'R' and B == 'S') : a += 1
        if (A == 'S' and B == 'P') : a += 1
        if (A == 'P' and B == 'R') : a += 1
        
        if (B == 'R' and A == 'S') : b += 1
        if (B == 'S' and A == 'P') : b += 1
        if (B == 'P' and A == 'R') : b += 1
        
    if (a > b) : print("Player 1")
    elif (a < b) : print("Player 2")
    else : print("TIE")