import sys
input = sys.stdin.readline

def DFS(n, val) :
    global answer
    if n >= N and answer < val:
        answer = val
        return

    for i in range(n, N) :
        DFS(i+2, val+arr[i][2])

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

answer = 0
DFS(0, 0)

print(answer)