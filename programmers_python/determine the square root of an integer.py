def solution(n):
    answer = -1
    
    for i in range(1, n+1) : 
        if (i * i == n) : return (i + 1) * (i + 1)
    
    return answer