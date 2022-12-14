for _ in range(int(input())) : 
    arr = list(map(str, input().split()))
    arr[0] = "god"
    answer = "".join(arr)
    
    print(answer)