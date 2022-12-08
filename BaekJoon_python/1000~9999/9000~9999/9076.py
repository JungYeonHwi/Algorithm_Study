T = int(input())

for i in range(T) : 
    List = list(map(int, input().split()))
    
    M = max(List)
    m = min(List)
    
    List.remove(M)
    List.remove(m)
    
    MM = max(List)
    mm = min(List)
    
    if(MM - mm >= 4) : print("KIN")
    else : print(sum(List))