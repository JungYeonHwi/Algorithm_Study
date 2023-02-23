N = int(input())
cards = list(map(int, input().split())) + [0] 

result = []
tmp = []

for i in range(N) :
    tmp.append(cards[i])

    if (cards[i+1] - cards[i]) != 1 :
        result.append(tmp)
        tmp = []

answer = 0

for j in result :
    answer += j[0]

print(answer)