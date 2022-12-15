def beat(i, j) : 
    if j - 1 < i : return 0
    
    answer = 0
    for a in range(i-1, j-1) : 
        answer += abs(arr[a] - arr[a+1])
        
    return answer

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(Q) : 
    i, j = map(int, input().split())
    print(beat(i, j))