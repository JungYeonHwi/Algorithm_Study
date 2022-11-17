n = int(input())
arr = list(map(int, input().split()))
answer = 0

def DFS(arr, total) :
    global answer
    if len(arr) == 2:
        answer = max(answer, total)
        return
    for i in range(1, len(arr)-1) :
        DFS(arr[:i] + arr[i+1:], total + (arr[i-1] * arr[i+1]))


DFS(arr, answer)
print(answer)