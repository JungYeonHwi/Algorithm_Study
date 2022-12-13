def solution(numbers, k):
    answer = 0
    
    value = numbers
    
    for i in range(0, len(numbers) * k) : 
        value.append(numbers[i])
    
    cnt = 2 * k - 2
    
    answer = value[cnt]
    
    return answer
