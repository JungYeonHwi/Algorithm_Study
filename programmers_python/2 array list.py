def solution(num_list, n):
    answer = []
    
    cnt = 0
    value = []
    
    for i in num_list : 
        cnt += 1
        value.append(i)
        
        if (cnt == n) : 
            answer.append(value)
            value = []
            cnt = 0
        else : continue
    
    return answer
