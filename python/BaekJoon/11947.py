T = int(input())

for _ in range(T):
    N = input()
    T5 = 5 * (10 ** (len(N)-1)) - 1
    n1 = ''
    n2 = ''
    
    if int(N) >= T5: 
        n1 = T5 + 1
        n2 = T5
        
    else:
        n1 = int(N)
        
        for i in N:
            n2 += str(9 -int(i))
        n2 = int(n2)
        
    print(n1 * n2)