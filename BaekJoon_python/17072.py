import sys
N, M = map(int, sys.stdin.readline().split())
asciiList = [list(map(int,input().split())) for _ in range(N)]

def intensity(tmp) :
    I = (2126 * tmp[0]) + (7152 * tmp[1]) + (722 * tmp[2])
    if I >= 0 and I < 510000 : return '#'
    elif I >= 510000 and I < 1020000 : return 'o'
    elif I >= 1020000 and I < 1530000 : return '+'
    elif I >= 1530000 and I < 2040000 : return '-'
    elif I >= 2040000 : return '.'

col = []
cnt = 0
result = []
tmp = []
for i in asciiList :
    col = []
    for j in i :
        tmp.append(j)
        cnt = cnt + 1
        if cnt == 3 :
            col.append(intensity(tmp))
            tmp = []
            cnt = 0
    result.append(col)

for i in result :
    for j in i :
        print(j, end='')
    print()