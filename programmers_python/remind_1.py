def solution(n):
    answer = 0
    List = []
    
    for i in range(1, n+1) : 
        if n % i == 1 : List.append(i)
    
    answer = min(List)
    
    return answer