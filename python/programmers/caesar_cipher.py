def solution(s, n):
    answer = ''
    
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for char in s :
        if char in low :
            value = low.find(char) + n
            answer += low[value % 26]
            
        elif char in up :
            value = up.find(char) + n
            answer += up[value % 26]
            
        else :
            answer += " "
    return answer