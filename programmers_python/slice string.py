def solution(my_str, n):
    answer = []
    
    for i in range(len(my_str)//n) :
        strSliced = ''
        strSliced = my_str[n * i : n * i + n]
        answer.append(strSliced)
        
    if len(my_str) % n != 0 :
        lastSliced = my_str[n * i + n : len(my_str)]
        answer.append(lastSliced)
    
    
    return answer