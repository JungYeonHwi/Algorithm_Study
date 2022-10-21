def solution(my_string, letter):
    answer = ''
    
    strList = list(map(str, my_string))
    
    for i in strList : 
        if i != letter : answer += i
    
    return answer
