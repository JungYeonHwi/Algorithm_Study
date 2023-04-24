from sys import stdin

input = stdin.readline

s = input().strip()

if len(s) < 4 :
    target = s[0]
    flag = True
    for n in s[1:]:
        if target != n:
            flag = False
            break
    if flag:
        print(s,s)
for start in range(1,1000):
    tmp = str(start)
    if tmp[0] == s[0]:
        tmp = ''
        for end in range(start,1000):
            tmp += str(end)
            if len(tmp) == len(s):
                if tmp == s:
                    print(start, end)
                    break
                else:
                    break
