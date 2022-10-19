def solution(n, k):
    answer = 0
    
    nSum = n * 12000
    kSum = k * 2000
    answer = nSum + kSum
    
    bonus = n // 10
    answer = nSum + kSum - bonus * 2000
    
    return answer