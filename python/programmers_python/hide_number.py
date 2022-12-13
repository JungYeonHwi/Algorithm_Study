def solution(phone_number):
    
    answer = ''
    
    phone_list = phone_number[:-4]
    
    for i in range(len(phone_list)) : 
        answer += '*'
        
    answer += phone_number[-4:]
    return answer