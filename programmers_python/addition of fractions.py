import math

def solution(denum1, num1, denum2, num2):
    
    answer = []
    
    if max(num1,num2)%min(num1,num2) == 0 :
        tmp =  max(num1,num2) // min(num1,num2)
        if num1 <= num2 :
            answer = [denum1 * tmp + denum2, num2]
        else :
            answer = [denum2 * tmp + denum1, num1]
    
    else : answer = [denum2 * num1 + denum1 * num2, num1 * num2]

    div = 2
    while min(answer[0],answer[1]) >= div :
        if answer[0] % div == 0 and answer[1] % div == 0 :
            answer[0] = answer[0] // div
            answer[1] = answer[1] // div
        else : div += 1
        
    return answer