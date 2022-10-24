def solution(i, j, k):
    answer = 0
    
    for i in range(i, j + 1) : 
        numberList = list(map(if j == k : answer += 1int, str(i)))
        for j in numberList : 
            if j == k : answer += 1
    
    return answer