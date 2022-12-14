def solution(x):
    answer = True
    
    arr = list(map(int, str(x)))
    s = sum(arr)
    
    if x % s == 0 : answer = True
    else : answer = False
    
    return answer