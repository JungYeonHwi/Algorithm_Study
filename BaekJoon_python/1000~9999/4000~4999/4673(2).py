def gen(num) : 
    numList = list(map(int, str(num)))
    return num + sum(numList)

checkList = [0 for i in range(10001)]

for i in range(1, 100001) : 
    check = gen(i)
    if (check < 10001) : checkList[check] = 1
    
for i in range(1, 10001) : 
    if (checkList[i] != 1) : print(i)