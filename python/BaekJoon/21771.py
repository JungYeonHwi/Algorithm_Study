rrw, rcol = map(int, input().split(' '))
gr, gc, pr, pc = map(int, input().split(' '))

MAP = [list(input()) for i in range(rrw)]

cnt = 0
for i in range(rrw):
    for j in range(rcol):
        if MAP[i][j] == 'P':
            cnt += 1

if cnt == pr * pc:
    print(0)
else:
    print(1)