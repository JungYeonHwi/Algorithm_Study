import sys
input = sys.stdin.readline

while 1 :
    try : N, M = map(int, input().split())
    except : break
    answer = 0
    for num in range(N, M+1):
        cnt = set()
        s = str(num)
        for char in s : cnt.add(char)
        if len(s) == len(cnt) : answer += 1
    print(answer)