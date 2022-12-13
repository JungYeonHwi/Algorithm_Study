T = int(input())

for _ in range(T) : 
    C = int(input())
    
    A = C // 25
    C -= 25 * (C // 25)
    
    B = C // 10
    C -= 10 * (C // 10)
    
    D = C // 5
    C -= 5 * (C // 5)
    
    E = C // 1
    
    print(A, B, D, E)