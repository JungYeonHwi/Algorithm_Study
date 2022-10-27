n = int(input())

for i in range(n) : 
    ns, ss, nd = map(int, input().split())
    
    d = 0
    
    for j in range(ns) : 
        sd, nD = map(int, input().split())
        
        if nd * ss >= sd : d = d + nD
    
    f = f"Data Set {i+1}:"
    print(f)
    print(d)
    print()