from itertools import combinations

def solution(number):
    answer = 0
    
    numList = list(combinations(number, 3))
    for i in numList : 
        s = sum(list(i))
        if s == 0 : answer += 1
    return answer