maxScore = [100, 100, 200, 200, 300, 300, 400, 400, 500]
score = list(map(int, input().split()))

totalScore, hacker = 0, 0
for i in range(9):
    if score[i] > maxScore[i] : hacker = 1
    totalScore += score[i]
if hacker : print("hacker")
else :
    if totalScore >= 100 : print("draw")
    else : print("none")