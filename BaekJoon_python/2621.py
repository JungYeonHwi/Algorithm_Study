import sys
input = sys.stdin.readline

card = [list(input().split()) for _ in range(5)]
colors = [i[0] for i in card]
numbers = [int(i[1]) for i in card]

cntColor = {'R':0, 'B':0, 'Y':0, 'G':0}
cntNum = [0 for _ in range(11)]

for i in range(5):
    color, number = card[i][0], int(card[i][1])
    cntColor[color] += 1
    cntNum[number] += 1
    
sortNums = list(numbers)
sortNums.sort()
if 5 in cntColor.values() and sortNums[0]+1 == sortNums[1] and sortNums[1]+1 == sortNums[2] and sortNums[2]+1 == sortNums[3] and sortNums[3]+1 == sortNums[4] :
    score = max(numbers) + 900
elif 4 in cntNum :
    score = cntNum.index(4) + 800
elif 3 in cntNum and 2 in cntNum :
    score = cntNum.index(3) * 10 + cntNum.index(2) + 700
elif 5 in cntColor.values() :
    score = max(numbers) + 600
elif sortNums[0]+1 == sortNums[1] and sortNums[1]+1 == sortNums[2] and sortNums[2]+1 == sortNums[3] and sortNums[3]+1 == sortNums[4] :
    score = max(numbers) + 500
elif 3 in cntNum :
    score = cntNum.index(3) + 400
elif 2 in cntNum :
    first = cntNum.index(2)
    num1 = numbers.copy()
    for i in num1 :
        if i == first : numbers.remove(i)
    cntNum[first] = 0
    if 2 in cntNum :
        second = cntNum.index(2)
        score = max(first, second) * 10 + min(first, second) + 300
    else : score = first + 200
else : score = max(numbers) + 100

print(score)
