while 1 :
    n = int(input())
    if n == 0 : break
    else : 
        arr = [1 for _ in range(50)]
        for _ in range(n) : 
            value = list(map(int, input().split()))
            for i in value : 
                arr[i] = 0
                
    if sum(arr) == 1 : print("Yes")
    else : print("No")