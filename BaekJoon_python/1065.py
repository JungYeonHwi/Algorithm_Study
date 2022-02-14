num = int(input())
answer = 0

if num < 100 : answer = num
else : 
    answer = 99
    for i in range(100, num+1) : 
        List = list(map(int, str(i)))
        
        value1 = List[0]-List[1]
        value2 = List[1]-List[2]
        
        if(value1 == value2) : answer += 1

print(answer)