quack = 'quack'
duck = input()
visited = [0] * len(duck)

def find(start):
    global cnt
    j = 0
    first = 1
    for i in range(start, len(duck)):
        if duck[i] == quack[j] and not visited[i]: # 울음소리 비교
            visited[i] = 1
            if duck[i] == 'k':
                if first:
                    cnt += 1 # 오리가 연속으로 울면 한 마리로 치기 때문에 처음만 count 해줌
                    first = 0 # 똑같은 오리가 울 경우에 다음부턴 count 안해주기 위해서
                j = 0 # 마지막 문자인 k까지 나왔으면 다시 q부터 찾아서 비교해야 함
            
            else:
                j += 1 # k가 아니면 순서대로 다음 문자를 비교하기 위해 index ++

if len(duck) % 5 != 0: # 입력된 문자열의 길이가 5의 배수가 아니라면 올바르지 않은 울음소리임
    print(-1)
    exit() # -1을 출력하고 exit를 해주어야 프로그램이 종료되어 다음 for문 실행이 안됨

cnt = 0 # 오리의 수
for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        find(i)

if cnt == 0 or not all(visited): # 오리의 수가 0마리거나 모든 문자를 방문하지 않았을 경우
    print(-1) # 올바르지 않은 울음소리

else: # 올바른 울음소리일 경우 오리의 수 출력
    print(cnt)
