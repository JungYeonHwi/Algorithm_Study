def gen(n) : 
    
    List = []
    nSum = 0
    
    for i in str(n):
        List.append(i)
        nSum = nSum + int(i)
    nSum += n
    return(nSum)
    
checkList = [0 for i in range(10001)]

for i in range(1, 10001) : 
    check = gen(i)
    if (check < 10001) : checkList[check] = 1
    
for i in range(1, 10001) : 
    if (checkList[i] != 1) : print(i)