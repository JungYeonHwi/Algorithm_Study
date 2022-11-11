def fac(n) : 
    if n == 0 : return 1
    else : return n * fac(n-1)
    
facNum = [fac(i) for i in range(21)]

num = int(input())

if num == 0 : print("NO")
else : 
    for i in range(20, -1, -1) :
        if num >= facNum[i] : num -= facNum[i]
        
    if num == 0 : print("YES")
    else : print("NO")