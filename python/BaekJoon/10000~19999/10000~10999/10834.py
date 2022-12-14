M = int(input())

resultDir = 0
resultCnt = 1

for _ in range(M) :
    first, second, dir = map(int, input().split())
    resultDir = resultDir ^ dir
    resultCnt = resultCnt // first * second

print(resultDir, resultCnt)