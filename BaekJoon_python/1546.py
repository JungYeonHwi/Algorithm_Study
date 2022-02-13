N = int(input())
gradeList = list(map(int, input().split()))
answerList = []

M = max(gradeList)

for i in gradeList : 
    answerList.append(i/M*100)
    
print(sum(answerList)/len(answerList))