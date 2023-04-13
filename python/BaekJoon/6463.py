while 1 :
    result = 1
    i = 0

    try : 
        n = int(input())
        while i != n : 
            i += 1
            result *= i
        while 1 : 
            check = result % 10
            if check : 
                break
            
            result //= 10
        
        print(f"{n:5} -> {check}")
    except : break