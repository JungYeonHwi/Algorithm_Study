import sys


while 1 :
    g, t, a, d = map(int, sys.stdin.readline().split())
    if (g == -1) : break
	
    pre = t * (t - 1) // 2 * g
	
    knockout = g * a + d
    
    x, y = 0, 0
    temp = 1
    while knockout > temp :
        x += temp
        temp *= 2
    
    y += temp - knockout
    x += pre

    print(f"{g}*{a}/{t}+{d}={x}+{y}")