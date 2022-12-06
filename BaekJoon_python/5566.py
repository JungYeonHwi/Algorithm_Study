N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
dice = [int(input()) for _ in range(M)]
current = 0
for idx, i in enumerate(dice) :
    current += i
    if current >= N-1 :
        print(idx+1)
        break

    move = board[current]
    current += move
    if current >= N-1 :
        print(idx+1)
        break