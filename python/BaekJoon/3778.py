import sys
for t in range(int(sys.stdin.readline())) :
    a = [0] * 26
    b = [0] * 26
    aStr = sys.stdin.readline()
    bStr = sys.stdin.readline()
    
    for i in range(len(aStr)-1) : a[ord(aStr[i]) - 97] += 1
    for i in range(len(bStr)-1) : b[ord(bStr[i]) - 97] += 1
    cnt = 0
    
    for i in range(26) :
        cnt += abs(a[i] - b[i])
    print("Case #%d: %d"%(t+1, cnt))