for _ in range(int(input())) : 
    n = int(input())
    arr1 = list(map(str, input().split()))
    arr2 = list(map(str, input().split()))
    
    arr1.sort()
    arr2.sort()
    
    answer = 0
    
    for i, j in zip(arr1, arr2) : 
        if i != j : answer += 1
    
    if answer == 0 : print("NOT CHEATER")
    else : print("CHEATER")