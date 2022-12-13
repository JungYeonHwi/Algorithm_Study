def solution(A, B):
    answer = -1
    i = 1
    
    if A == B : return 0
    
    while(i < len(A)) : 
        value = A[-1] + A[0:-1:]
        
        if value == B : return i
        
        A = value
        i += 1
    
    return answer