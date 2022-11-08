n = int(input())
arr = list(map(int, input().split()))
result = []

arr.sort()

for i in range(arr[0], len(arr) // 2) : 
    tmp = 0
    for j in arr : 
        tmp += abs(i - j)
    result.append([tmp, i])

result.sort()

print(result[0][1])