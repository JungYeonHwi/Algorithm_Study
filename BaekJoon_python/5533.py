n = int(input())
board = []

for _ in range(n) : 
    a, b, c = map(int, input().split())
    board.append([a, b, c])
    
reversedBoard = list(zip(*board))

answer = [0 for _ in range(n)]

for i in reversedBoard : 
    idx = 0
    for j in i :
        if i.count(j) == 1 : answer[idx] += j
        idx += 1
    idx = 0
    
for i in answer : print(i)