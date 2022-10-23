def solution(emergency):
    answer = []
    
    emergencyCopy = sorted(emergency, reverse = True)
    
    for j in emergency : 
        for i in emergencyCopy : 
            if i == j : answer.append(emergencyCopy.index(i) + 1)
    
    return answer
