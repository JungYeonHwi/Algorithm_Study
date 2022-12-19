for _ in range(int(input())) : 
    s, i, j = map(str, input().split())
    i = int(i)
    j = int(j)
    
    value = ""
    
    for idx in range(i, j) : 
        value += s[idx]
        
    s = s.replace(value, "", 1)
    
    print(s)