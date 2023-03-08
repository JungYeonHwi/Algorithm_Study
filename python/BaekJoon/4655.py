while 1 : 
    n = float(input())
    if n == 0.00 : break
    
    answer = 0
    value = 0
    
    for i in range(1, 274) : 
        
        value += 1 / (i+1)
        answer += 1
        
        if value >= n : 
            print(answer, "card(s)")
            break