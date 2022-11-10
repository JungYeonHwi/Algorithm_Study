import sys

n, m = map(int, sys.stdin.readline().split())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

answerList = arr1 + arr2
answer = ' '.join(map(str, sorted(answerList)))
print(answer)