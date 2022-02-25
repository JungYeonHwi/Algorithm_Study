while (1) : 
    n = int(input())
    if (n == -1) : break
    List = []
    
    for i in range(1, n) : 
        if (n % i == 0) : List.append(i)
    
    if (sum(List) == n) : print(n, " = ", " + ".join(str(i) for i in List), sep="")
    else:
        print(n, "is NOT perfect.")