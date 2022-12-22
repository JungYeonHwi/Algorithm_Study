import sys
input = sys.stdin.readline

for _ in range(int(input())) : 
    n = int(input())
    arr = []
    for i in range(n) : 
        arr.append(input().strip())
        
    arr.sort()
    
    flag = True

    for k in range(len(arr) - 1) : 
        if arr[k] == arr[k+1][:len(arr[k])] : 
            flag = False
            break
    
    if flag : print("YES")
    else : print("NO")