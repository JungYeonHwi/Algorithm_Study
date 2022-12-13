def solution(angle):
    answer = 0
    
    if angle == 90 : answer = 2
    elif angle == 180 : answer = 4
    elif 0 < angle and angle < 90 : answer = 1
    elif 90 < angle and angle < 180 : answer = 3
    
    return answer