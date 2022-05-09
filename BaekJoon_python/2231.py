def gen(n) : 

    nSum = 0
    
    for i in str(n) :
        nSum = nSum + int(i)
    nSum += n
    return(nSum)

n = int(input())
List = []

for i in range(1, n+1) : 
    if gen(i) == n : 
        print(i)
        break
    if i == n : print(0)