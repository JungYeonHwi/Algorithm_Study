N = int(input())
M, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
pen = M * K
cnt = 0
for p in A :
    if pen > 0 : 
        cnt += 1
        pen -= p
    else :
        break
if pen > 0 : print('STRESS')
else : print(cnt)
