for _ in range(int(input())) : 
    p, t = map(int, input().split())
    
    for i in range(1, t+1) : 
        if i % 7 == 0 : p -= 1
        if i % 4 == 0 : p += 1
    
    print(p)