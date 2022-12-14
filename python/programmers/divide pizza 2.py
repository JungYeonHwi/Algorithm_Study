import math

def lcm(a,b) :
    return (a * b) // math.gcd(a,b)

def solution(n):
    answer = 0

    if n % 6 == 0 : answer = n // 6
    else : answer = lcm(6, n) // 6
    
    return answer