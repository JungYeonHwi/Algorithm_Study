import sys
S,E,Q = map(str,sys.stdin.readline().rstrip().split())
s = {}
q = {}
attend = {}
cnt = 0

while True:
    try:
        talk, nickname = map(str, sys.stdin.readline().rstrip().split())
        if talk <= S:
            s[nickname] = '1'
        elif talk >= E and talk <= Q:
            q[nickname] = '1'
    except:
        break

for i in q:
    if i in s:
        cnt += 1

print(cnt)
