def solution(n):
    answer = 0
    
    a = n // 2
    
    for i in range(1, a + 1) : 
        check = 0
        for j in range(i, a + 2) : 
            check += j
            
            if check > n : break
            if check == n : answer += 1
            
    answer += 1
    
    return answer