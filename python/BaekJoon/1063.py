k, r, n = input().split()
moves = [input() for i in range(int(n))]

m = {'R':[0,1], 'L':[0,-1], 'B':[-1,0], 'T':[1,0],
     'RT':[1,1], 'LT':[1,-1], 'RB':[-1,1], 'LB':[-1,-1]}

alpha = {chr(i):ord(chr(i))-ord('A') for i in range(65, 73)}
rev_alpha = {i:chr(i+65) for i in range(8)}
kx, ky = int(k[1])-1, alpha[k[0]]
rx, ry = int(r[1])-1, alpha[r[0]]

maps = [[0]*8 for _ in range(8)]

for i in range(len(moves)):
    move = m[moves[i]]
    nkx, nky = kx + move[0], ky + move[1]
    if nkx < 0 or nky < 0 or nkx >= 8 or nky >= 8:
        continue

    if nkx == rx and nky == ry:
        nrx, nry = rx + move[0], ry + move[1]

        if nrx < 0 or nry < 0 or nrx >= 8 or nry >= 8:
            continue
        else:
            kx, ky = nkx, nky
            rx, ry = nrx, nry
    else:
        kx, ky = nkx, nky

print(rev_alpha[ky]+str(kx+1))
print(rev_alpha[ry]+str(rx+1))
