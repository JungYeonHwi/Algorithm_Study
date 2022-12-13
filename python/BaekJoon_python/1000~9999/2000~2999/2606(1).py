n = int(input()) # 총 컴퓨터의 수
m = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

graph = [[]*n for _ in range(n+1)] # 간선을 입력받을 경로

for _ in range(m) : # 간선을 입력 받을 경로
    a, b = map(int,input().split()) # 연결되어 있는 컴퓨터 번호 쌍 입력
    graph[a].append(b) # 번호 쌍 추가
    graph[b].append(a) # 번호 쌍 추가
    
cnt = 0 # 정답 변수
visited = [0]*(n+1) # 방문한 것을 확인하기 위한 변수

def DFS(start) : # DFS 함수
    global cnt  # 정답 변수
    visited[start] = 1 # 방문한 것을 저장
    for i in graph[start] : # 연결된 것들 중에서 확인
        print(i)
        if visited[i] == 0 : # 방문하지 않은 것을 확인
            DFS(i) # 방문하기 위해 DFS 반복
            cnt += 1 # 정답 증가
 
DFS(1) # 1번 컴퓨터가 연결된 것을 확인
print(cnt) # 정답 출력