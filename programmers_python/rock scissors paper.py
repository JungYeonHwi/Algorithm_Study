def solution(rsp):
    answer = ''
    
    rspList = list(map(str, rsp))
    
    for i in rspList : 
        if i == '2' : answer += '0'
        elif i == '0' : answer += '5'
        elif i == '5' : answer += '2'
    
    return answer
