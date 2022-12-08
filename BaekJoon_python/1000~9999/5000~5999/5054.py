t = int(input())

for i in range(t) :
    n = int(input())
    List = list(map(int, input().split()))
    res = 0
    
    List.sort()
    
    for k in range(1, len(List)) : 
        res = res + (List[k] - List[k-1])
        
    print(res * 2)