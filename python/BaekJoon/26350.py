for _ in range(int(input())) : 
    arr = list(map(int, input().split()))
    del arr[0]
    value = arr[0]
    chk = 0
    for i in range(1, len(arr)) : 
        if value * 2 > arr[i] : 
            chk = 1
            break
        
        value = arr[i]

    print("Denominations:", *arr)
    if chk : print("Bad coin denominations!")
    else : print("Good coin denominations!")
    
    print()