for _ in range(int(input())) : 
    x, y = map(int, input().split())
    answer = ""
    
    if x == y : 
        if x == 0 : answer = "No Number"
        elif x % 2 == 0 : answer = str(x * 2)
        else : answer = str(2 * y - 1)
    else : 
        if y == (x - 2) : 
            if y % 2 == 0 : answer = str(2 * y + 2)
            else : answer = str(2 * y + 1)
        else : answer = "No Number"
        
    print(answer)
            