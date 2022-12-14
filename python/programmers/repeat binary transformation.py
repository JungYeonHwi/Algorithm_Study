def solution(s):
    answer = [0, 0]
    sList = list(map(int, s))
    tmp = ""
    
    while 1 : 
        if (sList[0] == 1 and len(sList) == 1) : return answer
        else : 
            after = 0
            answer[0] += 1
            for i in sList : 
                if i == 0 : answer[1] += 1
                else : after += 1
                
        sList = list(map(int, str(bin(after)[2::])))
    
    return answer