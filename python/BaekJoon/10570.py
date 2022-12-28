for _ in range(int(input())) : 
    n = int(input())
    
    arr = [0 for _ in range(1001)]
    
    for i in range(n) : 
        arr[int(input())] += 1
        
    m = max(arr)
    
    answer = arr.index(m)
    
    print(answer)