import sys

scores = 0

for _ in range(10) :
    score = int(sys.stdin.readline())
    pre = scores
    scores += score
    if scores >= 100 :
        if abs(100-scores) > abs(100-pre) :
            scores = pre
        break
print(scores)