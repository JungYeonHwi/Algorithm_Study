def solution(n):
    answer = 0
    List = []
    
    while (n > 0) : 
        List.append(n % 10)
        n = n // 10
        
    List.sort()
    List.reverse()
    
    answer = int("".join(map(str, List)))
    
    return answer