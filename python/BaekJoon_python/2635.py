n = int(input())

answer = []
for i in range(1, n + 1) :
    arr = [n]
    arr.append(i)

    idx = 1
    while 1 :
        next = arr[idx - 1] - arr[idx]
        if next < 0 : break
        arr.append(next)
        idx += 1

    if len(answer) < len(arr) :
        answer = arr

print(len(answer))
print(*answer)