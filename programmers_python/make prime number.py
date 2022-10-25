from itertools import combinations
import math

def solution(nums):
    answer = 0

    com = list(combinations(nums, 3))
    
    for i in com : 
        one = list(i)
        n = sum(one)
        
        chk = 0
    
        for i in range (2, int(math.sqrt(n) + 1)) :
            if n % i == 0 : chk = 1
        
        if chk == 0 : answer += 1
            
    return answer