def solution(my_string, num1, num2):
    answer = ''
    
    strList = list(map(str, my_string))
    
    value = strList[num1] 
    strList[num1] = strList[num2]
    strList[num2] = value
    
    answer = "".join(strList)
    
    return answer
