T = int(input())

for _ in range(T) : 
    N = int(input())
    cn = 0
    gn = 0
    
    for n in range(N) : 
        C, G = map(float, input().split())
        
        cn += C
        gn += C * G
        
    GPA = gn / cn
    print(int(cn), '%.1f' %GPA)