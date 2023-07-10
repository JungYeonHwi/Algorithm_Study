import sys
input = sys.stdin.readline

N = int(input())

answer = 0
for i in range(N):
    answer += 1
    if str(i).find("50") > -1:
        answer += 1
print(answer)