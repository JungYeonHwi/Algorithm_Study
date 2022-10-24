import re

def solution(my_string):
    answer = 0
    
    numbers = list(map(int, re.findall(r'\d+', my_string)))
    
    answer = sum(numbers)
    return answer