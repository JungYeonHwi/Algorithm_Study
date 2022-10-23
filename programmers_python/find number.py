def solution(num, k):
    answer = -1
    
    numStr = str(num)
    
    for i in range(0, len(numStr)) :
        if k == int(numStr[i]) : 
            answer = i + 1
            break
    
    return answer
