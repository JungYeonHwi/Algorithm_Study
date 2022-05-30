def solution(numbers):
    answer = []
    
    for i in range(len(numbers) - 1) : 
        for j in range(i+1, len(numbers)) : 
            value = numbers[i] + numbers[j]
            
            if value not in answer : answer.append(value)
            
    answer.sort()
    
    return answer