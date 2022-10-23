def slopee(x1, y1, x2, y2) :
    
    value = 0
    
    if (x2 - x1 == 0) : value = 1
    else : value = float((y2 - y1) / (x2 - x1))
    return value

def solution(dots):
    answer = 0
    
    sloppeList = []
    
    for i in range(0, len(dots)) : 
        x1, y1 = map(int, dots[i])
        
        for j in range(i+1, len(dots)) : 
            x2, y2 = map(int, dots[j])
            
            value = slopee(x1, y1, x2, y2)
            
            if value in sloppeList : return 1
            else : sloppeList.append(value)
            
    return answer