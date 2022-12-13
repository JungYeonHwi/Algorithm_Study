def solution(array):
    answer = 0
    
    for i in array : 
        iStr = str(i)
        for j in iStr : 
            if j == "7" : answer += 1
    
    return answer
