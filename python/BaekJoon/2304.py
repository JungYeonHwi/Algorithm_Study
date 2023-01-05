n = int(input())

arr = []
answer = 0
for i in range(n) :
    a,b = map(int,input().split())
    arr.append([a,b])
    
arr.sort()

i = 0
for l in arr :
    if l[1] >answer :
        answer = l[1]
        idx = i
    i += 1

height = arr[0][1]

for i in range(idx) :
    if height < arr[i+1][1] :
        answer += height * (arr[i+1][0]-arr[i][0])
        height = arr[i+1][1]
    else :
        answer += height * (arr[i+1][0] - arr[i][0])

height = arr[-1][1]

for i in range(n-1, idx, -1) :
    if height < arr[i-1][1] :
        answer += height * (arr[i][0]-arr[i-1][0])
        height = arr[i-1][1]
    else :
        answer += height * (arr[i][0] - arr[i-1][0])

print(answer)
