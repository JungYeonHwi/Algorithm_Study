import math

def solution(a, b):
    answer = 2
    d = 2
    
    value = math.gcd(a, b)
    a = a // value
    b = b // value
    
    if a % b == 0 : return 1
    
    n = b
    primeList = []
    
    for i in range(2, n+1) : 
        if n % d == 0 :
            primeList.append(d)
            n = n // d
        else : d += 1
        
    primeList = list(set(primeList))
    
    for i in primeList : 
        if i == 2 or i == 5 : answer = 1
        else : return 2
    
    return answer