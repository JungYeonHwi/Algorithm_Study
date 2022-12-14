N = int(input())
List = list(map(int, input().split()))

count = 0

for i in List : 
    error = 0
    if i == 1 : count += 0
    else : 
        for k in range(2, i) : 
            if (i % k == 0) : error += 1
        if (error == 0) : count += 1
        
            
print(count)