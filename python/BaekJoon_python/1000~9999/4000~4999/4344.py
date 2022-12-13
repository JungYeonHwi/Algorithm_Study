C = int(input())

for i in range(C) : 
    List = list(map(int, input().split()))
    avg = sum(List[1:]) / List[0]
    count = 0
    
    for idx in List[1:] :
        if (idx > avg) : count = count + 1
    rate = count/List[0] * 100
    
    print(f'{rate:.3f}%')
        