import sys
n = int(sys.stdin.readline().strip())
arr = sys.stdin.readline().strip()

ck = [1] * len(arr)
answer = 0

for i in range(len(arr)-3) : 
  if arr[i:4+i] == 'pPAp' :
    if sum(ck[i:4+i])== 4 :
      answer += 1
      ck[i], ck[i+3] = 0, 0

print(answer)