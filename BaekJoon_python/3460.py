T = int(input())

for i in range(T) : 
    num = int(input())
    binNum = bin(num)
    binNumList = list(map(int, binNum[2:]))
    binNumList.reverse()
    
    List = []
    
    for i in range(len(binNumList)) : 
        if binNumList[i] == 1 : List.append(i)
        
    print(" ".join(map(str, List)))
