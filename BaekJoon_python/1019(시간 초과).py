n = int(input())
answer = [0 for _ in range(10)]

for i in range(1, n+1) : 
    num = list(map(str, str(i)))
    
    for j in num : 
        answer[int(j)] += 1
        
        
for i in answer : 
    print(i, end=" ")