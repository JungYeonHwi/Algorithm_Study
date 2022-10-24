def solution(array, n):
    answer = 0
    
    array.sort()
    minusList = []

    for i in array : 
        minusList.append(abs(n - i))
        
    minValue = min(minusList)
    idx = minusList.index(minValue)
    
    answer = array[idx]
        
    return answer