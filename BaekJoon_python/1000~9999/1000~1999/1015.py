n = int(input())
arr = list(map(int, input().split()))
sortedArr = sorted(arr)

answer = []

for i in range(n) : 
    idx = sortedArr.index(arr[i])
    answer.append(idx)
    sortedArr[idx] = -1

print(*answer)