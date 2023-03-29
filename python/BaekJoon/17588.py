arr = []

for _ in range(int(input())) : 
    n = int(input())
    arr.append(n)
    
    m = max(arr)
    ra = []
    
    for i in range(1, m+1) : 
        ra.append(i)
        
    ma = set(ra) - set(arr)
    
    if len(ma) != 0 : 
        for j in ma : print(j)
        
    else : print("good job")
    