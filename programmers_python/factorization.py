def solution(n):
    answer = []
    d = 2

    for i in range(2, n+1) : 
        if n % d == 0 :
            answer.append(d)
            n = n / d
            
        else : d += 1
        
    answer = list(set(answer))
    answer.sort()
    return answer