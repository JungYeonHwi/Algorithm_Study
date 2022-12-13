import sys

N = int(sys.stdin.readline())

power = [0, 0, 1]
maxTable = [0, 0, 1]
minTable = [0, 0, 1]

while (N < 0 and power[-1] > N) or (N > 0 and power[-1] < N) :
    if N <= maxTable[-1] and N >= minTable[-1] : break

    power.append(power[-1] * (-2))
    
    if power[-1] > 0 : 
        maxTable.append(maxTable[-2] + power[-1])
        minTable.append(minTable[-1] + power[-1])
    else :
        maxTable.append(maxTable[-1] + power[-1])
        minTable.append(minTable[-2] + power[-1])

answer = ''
now = N

for idx in range(len(power)-1, 1, -1) :
    if maxTable[idx] >= now and minTable[idx] <= now :
        answer += '1'
        now -= power[idx]
    else :
        answer += '0'

sys.stdout.write(answer)