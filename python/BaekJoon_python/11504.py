for i in range(int(input())) : 
    n, m = map(int, input().split())
    ex = input().split()
    x = int("".join([i for i in ex]))
    
    ey = input().split()
    y = int("".join([i for i in ey]))
    
    arr = input().split()
    new = arr + arr[:m-1]
    answer = 0
    
    for k in range(int(ex[0]), int(ey[0])+1)  : 
        idx = [i for i, value in enumerate(arr) if int(value) == k]
        
        for j in idx : 
            now = int("".join(new[j : j+m]))
            if x <= now <= y : answer += 1
            
    print(answer)