import heapq

N, M = map(int, input().split())
arr = []
ind = [1] * 1001 # 몇번째 인덱스에 있는 배열을 선택할 건지
maxVal = 0
hq = []
for i in range(N):
    li = list(map(int, input().split()))
    li.sort()
    maxVal = max(maxVal, li[0])
    arr.append(li)
    heapq.heappush(hq, (arr[i][0], i))

res = 10**9
while hq:
    front = heapq.heappop(hq)
    minVal = front[0]
    index = front[1]

    res = min(res, maxVal - minVal)
    if ind[index] == M:
        break
    heapq.heappush(hq, (arr[index][ind[index]], index))
    maxVal = max(maxVal, arr[index][ind[index]])
    ind[index] += 1

print(res)
