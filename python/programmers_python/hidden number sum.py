import re

def solution(my_string):
    answer = 0
    
    replaceString = re.sub(r'[^0-9]', '', my_string)
    
    numberList = list(map(int, replaceString))
    
    answer = sum(numberList)
    
    return answer
