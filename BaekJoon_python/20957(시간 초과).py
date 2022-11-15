import sys
input = sys.stdin.readline

for _ in range(int(input())) : 
    n = int(input())
    answer = 0
    
    if n == 1 : answer = 1
    else : 
        maxValue = int(str("9" * n))
        minValue = 10 ** (n-1)
        
        for i in range(minValue, maxValue+1) : 
            num = list(map(int, str(i)))
            numSum = sum(num)
            
            if numSum % 7 == 0 : 
                numMul = 1
            
                for j in num : 
                    numMul *= j
                    
                if numMul % 7 == 0 : answer += 1
        
    print(answer % (10 ** 9 + 7))
            