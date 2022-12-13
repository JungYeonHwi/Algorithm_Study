T = int(input())

for i in range(T) : 
    N = int(input())
    maxN = 0
    mName = ""
    
    for k in range(N) : 
        num, name = input().split()
        num = int(num)
        
        if(num > maxN) : 
            maxN = num
            mName = name
    print(mName)