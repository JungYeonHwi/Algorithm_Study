import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for i in range(n) :
    M = input()
    counter = defaultdict(lambda: 0)

    check = True
    nextFlag = False
    nextChar = ''
    
    for ch in M :
        if not check : break
        if nextFlag :
            if ch != nextChar:
                check = False
            nextFlag = False
            continue
        counter[ch] += 1
        if counter[ch] % 3 == 0 :
            nextFlag = True
            nextChar = ch
    
    if nextFlag : check = False
    
    if check : print("OK")
    else : print("FAKE")