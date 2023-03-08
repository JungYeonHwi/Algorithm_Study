for _ in range(int(input())) : 
    y, m, d = map(int, input().split())
    
    if 2007 - y > 18 : print("Yes")
    elif 2007 - y == 18 : 
        if m > 2 : print("No")
        elif m == 2 :
            if d >= 28 : print("No")
            else : print("Yes") 
        else : print("Yes")
    else : print("No")