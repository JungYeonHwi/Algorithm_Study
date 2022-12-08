K = int(input())

for i in range(K) : 
    List = list(map(int, input().split()))
    del List[0]
    
    print("Class", i+1)
    
    List.sort()
    diff = []
    
    for i in range(len(List)-1):
        diff.append(List[i+1] - List[i])

    print('Max', str(max(List))+',' ,'Min', str(min(List))+',', 'Largest gap', max(diff))