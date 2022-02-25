A, B = map(int, input().split())
List = []
idx = 1

while(len(List) < B) : 
    
    for i in range(idx) : 
        List.append(idx)
        
    idx += 1
    
print(sum(List[A-1 : B]))