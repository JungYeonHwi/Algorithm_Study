def solution(my_string):
    answer = ''

    lowerString = my_string.lower()
    strList = list(map(str, lowerString))
    
    strList.sort()
    
    for i in strList : 
        answer += i
    
    return answer
