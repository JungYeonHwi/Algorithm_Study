n = int(input())
arr = list(map(int, input().split()))

num = []
num.append(arr[0])

for i in range(1, n) : 
    num.append(num[i-1] + arr[i])
    
answer = 0

for i in range(n) : 
    answer += arr[i] * (num[n-1] - num[i])
    
print(answer)