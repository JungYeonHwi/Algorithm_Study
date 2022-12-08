t = int(input())

for _ in range(t) : 
    b = input()
    n = int(input())
    
    arr = []
    
    for j in range(n) : 
        candy = int(input())
        arr.append(candy)
        
    if sum(arr) % n == 0 : print("YES")    
    else : print("NO")