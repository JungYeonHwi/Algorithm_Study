import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int,input().rsplit())
ice = defaultdict(int)
minL, maxL, answer = sys.maxsize, 0, -1

for _ in range(n):
    g, x = map(int,input().rsplit())
    ice[x] = g
    maxL = max(maxL, x)
    minL = min(minL, x)

end, curr = minL, 0
for start in range(minL, maxL + 1):
    while end < maxL + 1 and end - start <= k * 2:
        if ice[end] == 0:
            end += 1
            continue
        curr += ice[end]
        end += 1
    answer = max(answer, curr)
    curr -= ice[start]
    

print(answer)
