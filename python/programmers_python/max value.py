def solution(numbers):
    answer = 0
    negativeNumbers = []
    positiveNumbers = []
    
    for i in numbers : 
        if i <= 0 : negativeNumbers.append(i)
        else : positiveNumbers.append(i)
    
    negativeNumbers.sort()
    positiveNumbers.sort()
    
    print(negativeNumbers)
    print(positiveNumbers)
    
    nMax = 0
    pMax = 0
    nMax2 = 0
    pMax2 = 0
    
    if len(negativeNumbers) >= 2 : nMax = negativeNumbers[0] * negativeNumbers[1]
    elif len(negativeNumbers) == 1 : nMax2 = negativeNumbers[0]
    
    if len(positiveNumbers) >= 2 : pMax = positiveNumbers[-1] * positiveNumbers[-2]
    elif len(positiveNumbers) == 1 : pMax2 = positiveNumbers[-1]
    
    if nMax > pMax : answer = nMax
    elif nMax < pMax : answer = pMax
    else : answer = nMax2 * pMax2
    
    return answer
