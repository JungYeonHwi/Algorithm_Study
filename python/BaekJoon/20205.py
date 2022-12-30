n, k = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for l in range(k):
        for j in range(n):
            for m in range(k):
                print(arr[i][j], end = ' ')
        print()