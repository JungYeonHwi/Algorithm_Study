def solution(numbers, direction):
    answer = []
    
    value = []
    
    if direction == "left" :
        value = numbers[0]
        numbers.remove(value)
        answer = numbers
        answer.append(value)
    else : 
        value = numbers[-1]
        numbers.remove(value)
        answer = numbers
        answer.insert(0, value)
            
    return answer
