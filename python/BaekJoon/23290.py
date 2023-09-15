from collections import defaultdict
 
M, S = map(int, input().split())
board = [[0] * 5 for _ in range(5)]
SMELL = 3
 
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# 1  2  3  4  5  6  7  8
dy8 = ('NO USE', 0, -1, -1, -1, 0, 1, 1, 1)
dx8 = ('NO USE', -1, -1, 0, 1, 1, 1, 0, -1)
 
# ↑, ←, ↓, →
# 1  2  3  4
dy4 = ('NO USE', -1, 0, 1, 0)
dx4 = ('NO USE',  0, -1, 0, 1)
 
loc2fish= defaultdict(list) # 기존 물고기 저장 dict
moved_loc2fish = defaultdict(list) # 이동후의 물고기 dict
 
for i in range(M):
    y, x, d = tuple(map(int, input().split()))
    loc2fish[(y, x)].append(d)
 
shark_loc = tuple(map(int, input().split())) # 상어 위치
 
def check_range(y, x):
    return y < 1 or x < 1 or y > 4 or x > 4
 
 
def move_fishes():
    global moved_loc2fish
    moved_loc2fish = defaultdict(list)
 
    for loc, d_list in loc2fish.items():
        y, x = loc
        for d in d_list: # (y, x)에 저장된 물고기들의 이동 방향
            can_go = False # 이동 가능 플래그
            nd = d # nd를 바꿔가며 이동할 방향을 정함
            for i in range(8):
                ny = y + dy8[nd]
                nx = x + dx8[nd]
 
                if check_range(ny, nx) or board[ny][nx] > 0 or (ny, nx) == shark_loc:
                    # 이동이 불가능 한 경우 반시계 방향으로 nd 조정
                    nd = nd - 1 if nd != 1 else 8
                    continue
                else:
                    # 이동이 가능한 경우
                    can_go = True # 이동 가능 플래그 기록
                    moved_loc2fish[(ny, nx)].append(nd) # 이동한 물고기 dict에 추가
                    break
            if not can_go:
                # 어느 방향으로도 이동할 수 없는 경우 현재 물고기 정보를 이동한 물고기 dict에 추가함
                moved_loc2fish[loc].append(d)
 
 
 
best_shark_move = None # 조건에 따라 가장 적합한 상어의 움직임 정보를 포함
def move_shark(shark, route, count, delete_loc):
    if len(route) != 0:
        if shark not in delete_loc: # 이미 방문한 상어 위치가 아닌 경우
            count += len(moved_loc2fish[shark]) # 제외될 물고기 개수 추가
            delete_loc.append(shark) # 제외된 위치 추가
 
    if len(route) == 3: # 3번 움직인 경우
        global best_shark_move
        if best_shark_move == None: # best_shark_move가 None인 경우
            best_shark_move = (int(route), count, shark, delete_loc) # (움직임 우선순위, 제외된 물고기 수, 상어의 마지막 위치, 제외된 위치 배열)
        elif best_shark_move[1] < count or (best_shark_move[1] == count and best_shark_move[0] > int(route)):
            # best_shark_move 보다 제외된 물고기 수가 더 많거나, 제외된 물고기 수는 같으나 움직임의 우선순위가 더 높은 경우
            best_shark_move = (int(route), count, shark, delete_loc)
        return
 
    # 4방향으로 재귀함수를 호출하여 탐색
    for i in range(1, 5, 1):
        y, x = shark
        ny = y + dy4[i]
        nx = x + dx4[i]
        if check_range(ny, nx):continue
        else: move_shark((ny, nx), route+str(i), count, delete_loc.copy())
 
 
def delete_and_update_fishes():
    global loc2fish, moved_loc2fish, shark_move_result, shark_loc, best_shark_move
    _, _, shark_next_loc, deleted_loc = best_shark_move # 가장 적합한 상어 움직임 정보를 가져옴
    shark_loc = shark_next_loc # 상어 위치 갱신
 
    # deleted_loc에 저장된 위치의 물고기들을 삭제하고, 냄새를 남김
    for loc in deleted_loc:
        y, x = loc
        if moved_loc2fish[loc] != []:
            board[y][x] = SMELL # 처음 SMELL = 3, 바로 다음 구문에서 냄새를 전부 1씩 없애기 때문
            moved_loc2fish.pop(loc) # 이동한 물고기 정보에서 해당 위치 물고기 삭제
 
    # 격자에 포함된 냄새 정부를 모두 -1씩함
    for y in range(1, 5, 1):
        for x in range(1, 5, 1):
            if board[y][x] > 0:
                board[y][x] -= 1
 
    # 기존의 물고기 dict와 이동한 물고기 dict를 합침
    for k, v in moved_loc2fish.items():
        if v != []:
            loc2fish[k].extend(v)
    moved_loc2fish = defaultdict(list)
 
 
def simulation():
    # 1. 물고기 이동
    move_fishes()
 
    # 2. 상어 이동
    global best_shark_move
    best_shark_move = None
    move_shark(shark_loc, "", 0, [])
 
    # 3. 상어 이동에 따라 물고기 갱신
    delete_and_update_fishes()
 
for i in range(S):
    simulation()
 
# 남아있는 물고기 개수 출력
result = 0
for k, v in loc2fish.items():
    result += len(v)
print(result)
