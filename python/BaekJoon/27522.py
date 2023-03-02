import sys
input = sys.stdin.readline

score = []
for _ in range(8):
    a, b = input().split()
    m, s, ms = map(int, a.split(':'))
    score.append([m, s, ms, b]) 
score.sort()
r, b = 0, 0
if score[0][3] == 'R':
    r += 10
else:
    b += 10
if score[1][3] == 'R':
    r += 8
else:
    b += 8
for i in range(2, 8):
    if score[i][3] == 'R':
        r += 8 - i
    else:
        b += 8 - i
print('Red' if r > b else 'Blue')