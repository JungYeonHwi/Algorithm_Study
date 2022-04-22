n = int(input()) # 총 컴퓨터의 수
m = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

graph = [[]*n for _ in range(n+1)] # 간선을 입력받을 경로
for _ in range(m) : # 연결된 컴퓨터 수만큼 반복
    a, b = map(int,input().split()) # 연결되어 있는 컴퓨터 번호 쌍 입력
    graph[a].append(b) # 번호 쌍 추가
    graph[b].append(a) # 번호 쌍 추가
    
cnt = 0 # 정답
visited = [0]*(n+1) # 방문한 것을 확인하기 위한 변수

def dfs(start) : # dfs 함수
    global cnt # 정답
    visited[start] = 1 # 방문한 것을 저장
    for i in graph[start] : # 연결된 것들 중에서 확인
        if visited[i] == 0 : # 방문하지 않은 것을 확인
            dfs(i) # 방문하기 위해 dfs 반복
            cnt += 1 # 정답
 
dfs(1) # 1번 컴퓨터로만 연결된 것을 확인하면 됨
print(cnt) # 정답 출력