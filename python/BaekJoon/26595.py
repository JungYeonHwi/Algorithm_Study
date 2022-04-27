N = int(input())

arr = list(map(int,input().split()))

cntA, cntB, s, Max = 0, 0, 0, 0
ansA, ansB = 0, 0

for i in range(N):
    cntA = (N-i)//arr[1]
    cntB = (i//arr[3])
    s = arr[0] * cntA + arr[2] * cntB

    if s >= Max :
        Max = s
        ansA = cntA
        ansB = cntB

print(str(ansA)+" "+str(ansB))