def solution(a, b):
    answer = 0
    
    if(a == b) : answer = a
    elif (a < b) :
        for i in range(a,b+1) :
            answer = answer + a
            a = a + 1
    else : 
        for i in range(b,a+1) :
            answer = answer + b
            b = b + 1
        
    return answer