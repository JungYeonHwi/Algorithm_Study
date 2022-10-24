def solution(sides):
    answer = 0
    
    M = max(sides)
    m = min(sides)
    
    # M이 가장 긴 변인 경우
    for i in range(1, M+1) : 
        if i + m > M : 
            answer += 1
            
    # 나머지 한 변이 가장 긴 변인 경우
    value = M+1
    while (value < M + m) : 
        answer += 1
        value += 1
        
    return answer