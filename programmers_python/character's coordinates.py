def solution(keyinput, board):
    answer = [0, 0]
    
    for i in keyinput : 
        value = 0
        if i == "left" : 
            value = answer[0] - 1
            if abs(value) <= (board[0] - 1) // 2 : answer[0] -= 1
        if i == "right" : 
            value = answer[0] + 1
            if value <= (board[0] - 1) // 2 : answer[0] += 1
        if i == "up" : 
            value = answer[1] + 1
            if value <= (board[1] - 1) // 2 : answer[1] += 1
        if i == "down" : 
            value = answer[1] - 1
            if abs(value) <= (board[1] - 1) // 2 : answer[1] -= 1
               
    return answer