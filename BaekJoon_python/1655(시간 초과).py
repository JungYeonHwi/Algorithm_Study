n = int(input())
arr = []
for _ in range(n) : 
    arr.append(int(input()))
    arr.sort()
    
    if len(arr) % 2 == 0 : 
        print(arr[len(arr) // 2 - 1])
    else : print(arr[len(arr) // 2])