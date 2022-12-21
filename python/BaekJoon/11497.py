for _ in range(int(input())) : 
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    answer= 0
    
    for j in range(2, n) : 
        answer = max(answer, abs(arr[j] - arr[j-2]))
    print(answer)