for i in range(int(input())) : 
    heads = int(input())
    action = input()
    
    for j in action : 
        if j == "c" : heads += 1
        else : heads -= 1
        
        if heads == 0 : break

    
    print(f"Data Set {i+1}:")
    print(heads)
    print()