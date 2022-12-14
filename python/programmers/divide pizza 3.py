def solution(slice, n):
    answer = 0
    
    if n % slice == 0 : value = 0
    else : value = 1
    
    answer = n // slice + value
    
    return answer