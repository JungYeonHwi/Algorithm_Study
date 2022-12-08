def change(num) : 
    n = list(map(int, str(num)))
    s = sum(n)
    return s 

for _ in range(int(input())) : 
    num = list(map(int, input()))
    
    reversedNum = num[::-1]
    for idx, value in enumerate(reversedNum) : 
        if idx % 2 == 1 : 
            changeValue = value * 2
            
            if changeValue >= 10 : 
                reversedNum[idx] = change(changeValue)
            else : 
                reversedNum[idx] = changeValue
                
    s = sum(reversedNum)
    
    if s % 10 == 0 : print("T")
    else : print("F")