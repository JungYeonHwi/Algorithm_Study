def solution(n):
    answer = 0
    value = 1
    
    for i in range(1, 11) : 
        value *= i
        
        if value <= n : answer = i
        
    return answer