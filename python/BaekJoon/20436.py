from sys import stdin

l, r = map(str, stdin.readline().rstrip().split())
string = stdin.readline().rstrip()

keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
mo = 'yuiophjklbnm'

xl, yl, xr, yr = None, None, None, None

for i in range(len(keyboard)) :
    if l in keyboard[i] : xl, yl = i, keyboard[i].index(l)
    if r in keyboard[i] : xr, yr = i, keyboard[i].index(r)

ans = 0

for s in string :
    ans += 1
    if s in mo :
        for i in range(len(keyboard)) :
            if s in keyboard[i] :
                nx = i
                ny = keyboard[i].index(s)

                ans += abs(xr - nx) + abs(yr - ny)

                xr, yr = nx, ny
                break

    else :
        for i in range(len(keyboard)) :
            if s in keyboard[i] :
                nx = i
                ny = keyboard[i].index(s)

                ans += abs(xl - nx) + abs(yl - ny)

                xl, yl = nx, ny
                break

print(ans)