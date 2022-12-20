N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sortedArr = sorted(arr, key=lambda x:(-x[0], x[1], x[2]))
print(arr.index(sortedArr[0])+1)