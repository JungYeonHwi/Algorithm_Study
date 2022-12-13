T = int(input())

for _ in range(T) : 
    S = input()
    sSet = set(S)
    s = 2015
    List = []
    
    for i in sSet : 
        s -= int(ord(i))
        
    print(s)