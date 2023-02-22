for _ in range(int(input())) : 
    arr = list(map(int, input().split(":")))
    h = arr[0]
    m = arr[1]
    s = arr[2]
    
    hh = bin(h)[2:]
    mm = bin(m)[2:]
    ss = bin(s)[2:]
    
    while len(hh) != 6 : 
        hh = "0" + hh
    while len(mm) != 6 : 
        mm = "0" + mm
    while len(ss) != 6 : 
        ss = "0" + ss
    
    duf = ""
    
    for i in range(6) : 
        duf += hh[i]+mm[i]+ss[i]
        
    god = hh+mm+ss

    print(duf, god)