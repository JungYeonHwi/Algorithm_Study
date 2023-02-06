while 1 : 
    arr = list(map(str, input().split()))
    
    if arr[-1] == "#" : break
    
    Cheryl = 0
    Tania = 0
    
    for i in range(0, len(arr)-1) : 
        if arr[i] == "A" : Cheryl += 1
        else : 
            if int(arr[i]) % 2 == 0 : Tania += 1
            else : Cheryl += 1
            
    if Cheryl > Tania : print("Cheryl")
    elif Cheryl < Tania : print("Tania")
    else : print("Draw")