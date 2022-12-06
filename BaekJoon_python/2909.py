c, k = map(int, input().split())
if k == 0 : print(c)
else :
    t = 10 ** k
    n = c // t * t
    a = len(str(c)) - k
    if int(str(c)[a]) < 5 : print(n)
    else : print(n + t)