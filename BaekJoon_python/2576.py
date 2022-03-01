List = []

for i in range(7) : 
    n = int(input())
    
    if (n % 2 == 1) : List.append(n)
    
if (len(List) == 0) : print(-1)
else : 
    print(sum(List))
    print(min(List))