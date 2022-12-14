def solution(n):
    fib = [0 for i in range(n+1)]
    fib[1] = 1
    
    for i in range(2, n+1) :
        fib[i] = fib[i-2] + fib[i-1]
            
    answer = fib[-1] % 1234567

    return answer