from collections import defaultdict
import sys
input = sys.stdin.readline

while 1 : 
    n, m  = map(int, input().split())
    arr = defaultdict(bool)
    cnt = 0
    if n == m == 0 : break
    else : 
        for _ in range(n) : 
            arr[int(input())] = True
        for _ in range(m) : 
            if arr[int(input())] : cnt += 1
            
        print(cnt)