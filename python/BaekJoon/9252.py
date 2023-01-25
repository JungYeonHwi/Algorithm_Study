import sys
input = sys.stdin.readline

seq_1 = input().rstrip()
seq_2 = input().rstrip()

n = len(seq_1)
m = len(seq_2)

arr = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if seq_1[j-1] == seq_2[i-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

print(arr[m][n])

if arr[m][n] != 0:
    current_x = m
    current_y = n
    result = ""
    while current_x != 0 and current_y != 0:
        if seq_1[current_y-1] == seq_2[current_x-1]:
            result += seq_1[current_y-1]
            current_x -= 1
            current_y -= 1
        
        else:
            if arr[current_x][current_y] == arr[current_x-1][current_y]:
                current_x -= 1
            
            elif arr[current_x][current_y] == arr[current_x][current_y-1]:
                current_y -= 1

    print(result[::-1])
