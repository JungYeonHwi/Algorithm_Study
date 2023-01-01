import sys
input = sys.stdin.readline

def draw(n,idx):
    if n==1:
        stars[idx][idx] = '*'
        return ;
    l = 4*n-3

    for i in range(idx,l+idx):
        stars[idx][i]='*'
        stars[idx+l-1][i]='*'

        stars[i][idx]='*'
        stars[i][idx+l-1]='*'

    return draw(n-1,idx+2)

n = int(input())
lens = 4*n -3

stars = [[' ']*lens for _ in range(lens) ]

draw(n,0)

for i in range(lens):
    for j in range(lens):
        print(stars[i][j],end="")
    print()