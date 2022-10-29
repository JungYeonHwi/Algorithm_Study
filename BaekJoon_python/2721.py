def T(num) :
    answer = 0
    
    for i in range(1, num+1) : 
        answer += i
    
    return answer    

t = int(input())

for _ in range(t) : 
    n = int(input())
    answer = 0
    
    for i in range(1, n+1) : 
        t = T(i+1)
        answer += t * i
    
    print(answer)