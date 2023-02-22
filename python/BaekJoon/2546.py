t = int(input())

for i in range(t):
    value = input()
    answer = 0
    n, m = map(int, input().split())
    
    nArr = list(map(int, input().split()))
    mArr = list(map(int, input().split()))
    
    ns = sum(nArr)
    ms = sum(mArr)
    
    for i in range(n) : 
        if ns > nArr[i] * n and ms < nArr[i] * m : answer += 1
        
    print(answer)