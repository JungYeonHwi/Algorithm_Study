while (1) : 
    List = list(map(int, input()))
    
    if (List[0] == 0) : break
    else : 
        if List == List[::-1] : print("yes")
        else : print("no")