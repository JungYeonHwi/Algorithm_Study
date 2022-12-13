def solution(order):
    answer = 0
    
    strOrder = str(order)
    
    for i in strOrder : 
        if "3" == str(i) : answer += 1
        elif "6" == str(i) : answer += 1
        elif "9" == str(i) : answer += 1
    
    return answer
