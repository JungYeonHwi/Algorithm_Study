def gen(num) : 
    numList = list(map(int, str(num)))
    return num + sum(numList)

n = int(input())

for i in range(1, n+1) : 
    if gen(i) == n : 
        print(i)
        break
    if i == n : print(0)