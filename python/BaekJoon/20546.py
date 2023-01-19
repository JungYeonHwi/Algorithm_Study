n = int(input())
arr = input().split()

pm1, pj1 = n, 0
pm2, pj2 = n, 0
p2 = []

arr = list(map(int,arr))

for cost in arr:
    pj1 += pm1//cost
    pm1 = pm1%cost

    p2.append(cost)
    if len(p2) >= 4 : 
        if p2[0] > p2[1] > p2[2] :
            pj2 += pm2 // cost
            pm2 = pm2 % cost 
        elif p2[0] < p2[1] < p2[2] : 
            pm2 += pj2 * cost
            pj2 = 0 
        p2.pop(0)

if pm1 + arr[-1] * pj1 > pm2 + arr[-1] * pj2 : print('BNP')
elif pm1 + arr[-1] * pj1 < pm2 + arr[-1] * pj2 : print('TIMING')
else : print('SAMESAME')