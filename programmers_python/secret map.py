def solution(n, arr1, arr2):
    answer = []
    
    result = [[" "] * n for i in range(n)]
    arr1map = []
    arr2map = []
    
    for i in arr1 : 
        tmp = list(map(int, str(bin(i)[2:])))
        while len(tmp) < n : tmp.insert(0, 0)
        arr1map.append(tmp)
    
    for i in arr2 : 
        tmp = list(map(int, str(bin(i)[2:])))
        while len(tmp) < n : tmp.insert(0, 0)
        arr2map.append(tmp)

    for rkfh in range(0, n) : 
        for tpfh in range(0, n) : 
            if (arr1map[rkfh][tpfh] == 1) : result[rkfh][tpfh] = "#"
            if (arr2map[rkfh][tpfh] == 1) : result[rkfh][tpfh] = "#"
    
    for i in range(0, n) : 
        one = ''
        for j in range(0, n) : 
            one += result[i][j]
            
        answer.append(one)
    
    return answer