N, a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = "HAPPY"
t = arr[a-1][b-1]

if t < max([arr[i][b-1]for i in range(N)]) or t < max([arr[a-1][j]for j in range(N)]) :
    answer = "ANGRY"
    
print(answer)