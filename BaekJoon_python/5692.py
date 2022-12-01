import sys

def f(n) :
    return n * f(n-1) if n > 0 else 1

while 1 :
    n = sys.stdin.readline().rstrip()
    if n == '0' : break
    answer = 0
    for i in range(1, len(n)+1) :
        answer += int(n[len(n)-i]) * f(i)
    print(answer)