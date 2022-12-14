def solution(before, after):
    answer = 0
    
    for i in before : 
        after = after.replace(i, "", 1)
        
    if len(after) == 0 : answer = 1
    else : answer = 0
    
    return answer