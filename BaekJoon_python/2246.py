n = int(input())
D = []
C = []
arr = []

for _ in range(n) : 
    d, c = map(int, input().split())
    arr.append([d, c])
    
answer = 0

for i in range(n) : 
    flag = 0
    for j in range(n) : 
        if i != j :
            if arr[i][0] > arr[j][0] and arr[i][1] >= arr[j][1] : 
                flag = 1
                break
            if arr[i][1] > arr[j][1] and arr[i][0] >= arr[j][0] : 
                flag = 1
                break
    
    if flag == 0 : answer += 1
    
print(answer)