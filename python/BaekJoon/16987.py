n = int(input())
s = [0]*n
w = [0]*n

for i in range(n):
    s[i], w[i] = map(int, input().split())

res = 0 
def crash(idx, eggs):
    global res
    if idx == n:
        cnt = 0
        for i in range(n):
            if eggs[i] <= 0:
                cnt +=1
        if cnt > res:
            res = cnt
        return

    if eggs[idx] > 0:
        for i in range(n):
            flag = False
            if eggs[i] > 0 and i != idx:
                flag = True
                tmp = eggs[:]
                tmp[i] -= w[idx]
                tmp[idx] -= w[i]
                crash(idx+1, tmp)
        if not flag:
            crash(idx+1, eggs)
    else:
        crash(idx+1, eggs)

crash(0, s)
print(res)