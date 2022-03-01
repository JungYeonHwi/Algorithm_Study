for i in range(3) : 
    List = list(map(int, input().split()))
    one = List.count(1)
    zero = List.count(0)
    
    if (one == 3 and zero == 1) : print("A")
    elif (one == 2 and zero == 2) : print("B")
    elif (one == 1 and zero == 3) : print("C")
    elif (zero == 4) : print("D")
    elif (one == 4) : print("E")