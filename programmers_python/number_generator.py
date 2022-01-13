def solution(x, n):
    sum = x
    answer = []
    
    while(len(answer) != n) : 
        answer.append(sum)
        sum += x
        
    return answer