def solution(dots):
    answer = 0
    
    rkfh = []
    tpfh = []
    
    for i in dots : 
        rkfh.append(i[0])
        tpfh.append(i[1])
        
    rkfhSet = list(set(rkfh))
    tpfhSet = list(set(tpfh))
    
    rkfhSet.sort()
    tpfhSet.sort()
    
    answer = (abs(rkfhSet[1] - rkfhSet[0])) * (abs(tpfhSet[1] - tpfhSet[0]))
    
    return answer