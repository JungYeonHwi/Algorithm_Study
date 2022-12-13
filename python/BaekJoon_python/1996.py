N = int(input())
arr = ['.'*(N+2)] + ['.'+input()+'.' for _ in range(N)] + ['.'*(N+2)]
answer = []
for i in range(N): 
    i += 1
    s = ''
    for j in range(N) :
        j += 1
        if ord('0') <= ord(arr[i][j]) <= ord('9') : s += '*'
        else :
            bomb = 0
            for a in range(i-1, i+2) :
                for b in range(j-1, j+2) :
                    if ord('0') <= ord(arr[a][b]) <= ord('9') :
                        bomb += int(arr[a][b])
            s += str(bomb) if bomb < 10 else "M"
    answer.append(s)
    
for i in answer :
    print(i)