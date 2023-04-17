import sys
input = sys.stdin.readline

n = int(input())
score = {1: 0, 2: 0}
time = {1: 0, 2: 0}
ans = {1: 0, 2: 0}
state = 0 


for _ in range(n):
    team, t = input().split()
    team = int(team)
    m, s = map(int, t.split(':'))
    t = m * 60 + s
    score[team] += 1

    if state == 0:
        time[team] = t
        state = team
    elif state != 0 and score[1] == score[2]:
        ans[state] += t-time[state]
        state = 0

if state != 0:
    ans[state] += 60*48-time[state]

print('{:0>2}:{:0>2}'.format(ans[1]//60, ans[1] % 60))
print('{:0>2}:{:0>2}'.format(ans[2]//60, ans[2] % 60))