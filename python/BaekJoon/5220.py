for _ in range(int(input())) : 
    n, c = map(int, input().split())
    
    value = str(bin(n)[2:])

    while len(value) != 16 : 
        value = "0" + value

    check = value.count("1")
    
    if check % 2 == 0 : cc = 0
    else : cc = 1
    
    if cc == c : print("Valid")
    else : print("Corrupt")