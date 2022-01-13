def solution(n):
    answer = 0
    list = []
    
    for i in range(n) : 
        i += 1
        if (n % i == 0) : 
            list.append(i)
            
    answer = sum(list)
    
    return answer