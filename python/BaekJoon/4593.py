while 1 : 
    a = input()
    b = input()
    
    A = 0
    B = 0

    if a == "E" and b == "E" : break
    else : 
        for i, j in zip(a, b) : 
            if i == "R" and j == "S" : A += 1
            if i == "R" and j == "P" : B += 1
            if i == "S" and j == "R" : B += 1
            if i == "S" and j == "P" : A += 1
            if i == "P" and j == "R" : A += 1
            if i == "P" and j == "S" : B += 1
            
        print("P1:", A)
        print("P2:", B)
            