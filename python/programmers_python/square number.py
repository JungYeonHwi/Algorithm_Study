def solution(n):
    answer = 2
    
    for i in range(n//2) : 
        if i * i == n : answer = 1
    
    return answer