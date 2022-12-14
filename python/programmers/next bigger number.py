def solution(n):
    answer = 0
    strN = str(bin(n)[2::])
    nCnt = 0
    
    for i in strN : 
        if i == "1" : nCnt += 1
    
    for i in range(n+1, 1000000) : 
        num = bin(i)[2::]
        strNum = str(num)
        numCnt = 0
        
        for a in strNum : 
            if a == "1" : numCnt += 1
            
        if nCnt == numCnt : return i
            
    return answer