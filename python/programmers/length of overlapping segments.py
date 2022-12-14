def solution(lines):
    answer = 0
    
    start = 0
    end = 0
    
    arr = [0 for _ in range(200)]
    
    for i in lines : 
        start = min(i[0], i[1]) + 100
        end = max(i[0], i[1]) + 100
        
        for j in range(start, end) : 
            arr[j] += 1
    
    for i in arr : 
        if i >= 2 : answer += 1
    
    return answer