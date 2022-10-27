from xxlimited import Str


t = int(input())
for _ in range(t) : 
    a, b = map(str, input().split())
    
    chk = 1
    
    for i in range(len(a)) : 
        if a[i] != b[i] : chk = 0
        
    if chk == 1 : print("OK")
    else : print("ERROR")
    