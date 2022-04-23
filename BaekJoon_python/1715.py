import heapq # 우선순위 큐

N = int(input())

cardList = list(int(input()) for _ in range(N))
heapq.heapify(cardList)
result = 0


while len(cardList) != 1 :
    num1 = heapq.heappop(cardList)
    num2 = heapq.heappop(cardList)
    s = num1 + num2
    result += s
    heapq.heappush(cardList, s)

print(result)