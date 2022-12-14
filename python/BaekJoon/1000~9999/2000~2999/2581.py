M = int(input())
N = int(input())

List = []

for i in range(M, N+1) : 
    error = 0
    if i == 1 : pass
    else : 
        for k in range(2, i) : 
            if (i % k == 0) : error += 1
        if (error == 0) : List.append(i)
        
if (len(List) == 0) : print(-1)
else : 
    print(sum(List))
    print(min(List))