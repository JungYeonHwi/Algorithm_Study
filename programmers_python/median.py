def solution(array):
    answer = 0
    
    array.sort()
    
    if len(array) == 1 : answer = array[0]
    else : answer = array[(len(array) + 1) // 2 - 1]
    
    return answer