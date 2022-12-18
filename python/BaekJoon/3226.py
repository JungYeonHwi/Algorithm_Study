from sys import stdin

n = int(stdin.readline())

answer = 0

for i in range(n) : 
    s, d = stdin.readline().rstrip().split(" ")
    d = int(d)
    h, m = map(int, s.split(":"))
    
    endH = h
    endM = m + d

    if endM >= 60 : 
        endH += 1
        endM -= 60
    if endH >= 24 : 
        endH -= 24
    
    if 7 <= h <= 18 and 7 <= endH <= 18 : answer += d * 10
    elif (0 <= h <= 6 or 19 <= h <= 23) and (0 <= endH <= 6 or 19 <= endH <= 23) : answer += d * 5
    elif h == 18 and endH == 19 : answer += 10 * (60 - m) + 5 * endM
    elif h == 6 and endH == 7 : answer += 5 * (60 - m) + 10 * endM

print(answer)
    