dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def move(now_num):
    global horse

    now_x, now_y, now_d = horse[now_num]

    nx, ny, nd = now_x + dx[now_d], now_y + dy[now_d], now_d
    if nx < 0 or nx >= N or ny < 0 or ny >= N or chess_map[nx][ny] == 2:
        if 0 <= nd <= 1:
            nd = (nd + 1) % 2
        else:
            nd = (nd - 1) % 2 + 2
        nx, ny = now_x + dx[nd], now_y + dy[nd]
        horse[now_num][2] = nd

        if not (0 <= nx < N) or not (0 <= ny < N) or chess_map[nx][ny] == 2:
            return False

    if chess_map[nx][ny] == 0:
        index = chess_map_horse[now_x][now_y].index(now_num)
        new_arr = chess_map_horse[now_x][now_y][index:]

        chess_map_horse[nx][ny] += new_arr

        if new_arr:
            for child in new_arr:
                horse[child][0], horse[child][1] = nx, ny

        chess_map_horse[now_x][now_y] = chess_map_horse[now_x][now_y][:index]
        horse[now_num] = [nx, ny, nd]

    elif chess_map[nx][ny] == 1:
        index = chess_map_horse[now_x][now_y].index(now_num)
        new_arr = chess_map_horse[now_x][now_y][index:]
        chess_map_horse[nx][ny] += new_arr[::-1]

        if new_arr:
            for child in new_arr:
                horse[child][0], horse[child][1] = nx, ny

        chess_map_horse[now_x][now_y] = chess_map_horse[now_x][now_y][:index]
        horse[now_num] = [nx, ny, nd]

    return check_end()


def check_end():
    for i in range(N):
        for j in range(N):
            if len(chess_map_horse[i][j]) >= 4:
                return True
    return False


N, K = map(int, input().split())

chess_map = [list(map(int, input().split())) for _ in range(N)]
chess_map_horse = [[[] for _ in range(N)] for _ in range(N)]
horse = []
for i in range(K):
    x, y, d = map(int, input().split())
    horse.append([x - 1, y - 1, d - 1])
    chess_map_horse[x - 1][y - 1].append(i)

time = 0
flag = False
while True:

    if time > 1000:
        time = -1
        break
    if flag is True:
        break
    time += 1
    for i in range(K):
        if move(i):
            flag = True
            break

print(time)
