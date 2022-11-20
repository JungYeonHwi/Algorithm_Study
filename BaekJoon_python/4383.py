while 1 : 
    try : 
        arr = list(map(int, input().split()))
        nums = arr[1:]
        n = [i for i in range(1, arr[0])]
        check = []
        for i in range(arr[0]-1) : 
            check.append(abs(nums[i]-nums[i+1]))
    
        if sorted(check) == n : print("Jolly")
        else : print("Not jolly")
            
    except : break