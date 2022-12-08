import sys
input = sys.stdin.readline
from collections import defaultdict

while 1 :
    N, M = map(int, input().split())
    if not N and not M : break
    rankers = defaultdict(int)
    answer = []
    m = 0
    for _ in range(N) :
        a = list(map(int, input().split()))
        for num in a :
            rankers[num] += 1
            if rankers[num] > m :
                m = rankers[num]
                answer = [num]
            elif rankers[num] == m :
                answer.append(num)
    for first in answer :
        del rankers[first]
    answer = []
    m = 0
    
    for num in rankers :
        if rankers[num] > m :
            m = rankers[num]
            answer = [num]
        elif rankers[num] == m :
            answer.append(num)
    print(*sorted(answer))