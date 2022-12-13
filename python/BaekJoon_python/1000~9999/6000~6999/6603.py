from itertools import combinations

while 1 : 
    data = list(map(int, input().split()))
    
    if data[0] == 0 : break
    else : 
        result = list(combinations(data[1:], 6))
        answer = []
        
        for i in range(0, len(result)) : 
            one = []
            for j in result[i] : 
                one.append(j)
                
            for k in one : 
                print(k, end=" ")
            print()
        print()