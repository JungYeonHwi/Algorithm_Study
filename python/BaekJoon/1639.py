import sys

def isLucky(x) :
    mid = len(x) // 2
    sum1 = sum2 = 0
    for i in range(mid):
        sum1 += int(x[i])
        sum2 += int(x[len(x)-1-i])
    if sum1 == sum2:
        return True
    else:
        return False


s = sys.stdin.readline().strip()
if len(s) % 2 == 0 :
    chk = len(s)
else :
    chk = len(s)-1
while chk > 0 :
    i = 0
    ans = 0
    while i+chk <= len(s) :
        if isLucky(s[i:i+chk]) :
            ans = chk
            break
        i += 1
    if ans :
        break;
    chk -= 2
print(ans)