def solution(sides):
    answer = 0
    
    sides.sort()
    
    if sides[0] + sides[1] <= sides[2] : answer = 2
    else : answer = 1
    
    return answer