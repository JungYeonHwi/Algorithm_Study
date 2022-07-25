import sys
input = sys.stdin.readline
 
n = int(input())
score, time = [], []
result = []
 
for _ in range(n):
    flag = list(map(int, input().split()))
 
    if flag[0]:    # 입력이 1 ? ? 인 경우
        score.append(flag[1])
        time.append(flag[2])
 
    if time:
        time[-1] -= 1
        if not time[-1]:
            result.append(score.pop())
            time.pop()
 
print(sum(result))