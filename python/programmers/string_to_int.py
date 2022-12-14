def solution(s):
    answer = 0
    
    list = "".join(s)
    minus_list = ""
    
    if(list[0] == '-') : 
        for i in range(len(list)-1) : 
            i += 1
            minus_list += list[i]
            answer = (-1) * int(minus_list)
    
    else : 
        answer = int(s)
        
    return answer