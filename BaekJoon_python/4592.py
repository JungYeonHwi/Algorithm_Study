while 1 : 
    arr = list(map(int, input().split()))
    
    if arr[0] == 0 : break
    else : 
        stack = []
        for i in arr[1:] : 
            if i not in stack : 
                print(i, end=" ")
                stack.append(i)
        print("$")