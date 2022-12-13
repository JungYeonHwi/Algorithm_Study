import sys
arr = str(sys.stdin.readline().rstrip())
r = 1
c = len(arr)

for i in range(1,len(arr)+1) :
    if len(arr) % i == 0 :
        if r < i and i <= len(arr) // i  :
            r = i
            c = len(arr) // i
            
answer = [[] for _ in range(r)]
cnt = 0

for i in range(c) :
    for k in range(r) :
        answer[k].append(arr[cnt])
        cnt +=1

for i in range(r) : print(''.join(answer[i]), end='')