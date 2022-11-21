n, m = map(int, input().split())
board = []

end = "#" * (m * 5 + 1)

one = "................"
two = "****............"
three = "********........"
four = "************...."
five = "****************"

answer = [0 for _ in range(5)]

for _ in range(5 * n + 1) : 
    value = input()
    board.append(value)
    
    if end in board : 
        board.remove(end)

store = ["" for _ in range(m)]

for i in range(len(board)) : 
    board[i] = board[i].replace("#", "")

for i in range(len(board)) : 
    tmp = ''
    cnt = 0
    for j in range(len(board[i])) : 
        tmp += board[i][j]
        if len(tmp) == 4 : 
            store[cnt] += tmp
            tmp = ''
            cnt += 1
    
    
    if len(store[0]) == 16 : 
        for idx in store : 
            if idx == one : answer[0] += 1
            if idx == two : answer[1] += 1
            if idx == three : answer[2] += 1
            if idx == four : answer[3] += 1
            if idx == five : answer[4] += 1
            
        store = ["" for _ in range(m)]
        
print(*answer)