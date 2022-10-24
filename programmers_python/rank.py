def solution(score):
    answer = [0 for i in range(len(score))]
    scoreList = []
    
    for i in score : 
        scoreList.append(i[0] + i[1])
        
    copy = list(set(scoreList))
    copy.sort(reverse = True)
    
    value = 1
    
    for i in copy : 
        idxList = list(filter(lambda x : scoreList[x] == i, range(len(scoreList))))

        if (len(idxList) == 1) : 
            answer[idxList[0]] = value
            
        else : 
            for i in range(0, len(idxList)) : 
                answer[idxList[i]] = value   
        value += len(idxList)
    
    return answer