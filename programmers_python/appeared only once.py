def solution(s):
    answer = ''
    
    lowList = [0 for i in range(26)]
    
    value = s
    
    for i in s : 
        lowList[ord(i)-97] += 1
            
    for i in range(0, len(lowList)) : 
        if lowList[i] == 1 : answer += chr(i+97)
    
    answerList = list(map(str, answer))
    answerList.sort()
            
    answer = "".join(answerList)
    
    return answer