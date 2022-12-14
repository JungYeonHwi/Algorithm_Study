def solution(s):
    answer = ''
    
    list = []
    
    for i in s : 
        list.append(i)
        list.sort(reverse=True)
        
    answer = "".join(list)
    
    return answer