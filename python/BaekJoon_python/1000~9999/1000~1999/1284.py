while(1) : 
    N = int(input())
    
    if (N == 0) : break
    else : 
        List = list(map(int, str(N)))
        s = 0
        
        for i in List : 
            if (i == 0) : s += 4
            elif (i == 1) : s += 2
            else : s += 3
        s += len(List) + 1
        print(s)