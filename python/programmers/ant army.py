def solution(hp):
    answer = 0
    
    first = hp // 5
    second = ((hp - first * 5) // 3)
    third = hp - first * 5 - second * 3
    answer = first + second + third
    
    return answer
