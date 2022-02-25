T = int(input())

for i in range(T) : 
    List = list(map(int, input().split()))
    answer = []
    
    for k in List : 
        if (k % 2 == 0) : answer.append(k)
        
    print(sum(answer), min(answer))