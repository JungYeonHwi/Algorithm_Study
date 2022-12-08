N = int(input())
List = []

for i in range(N) : 
    L, D = input().split("-")
    intValue = int(D)
    
    value = 0
    
    for k in range(3) : 
        value += (ord(L[k]) - 65) * 26 ** (2-k)
    
    answer = abs(value - intValue)
    if (answer <= 100) : print("nice")
    else : print("not nice")