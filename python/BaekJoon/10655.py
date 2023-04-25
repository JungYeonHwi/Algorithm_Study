n = int(input())
axis = [0] * n
for i in range(n) : 
  axis[i] = list(map(int,input().split()))
  maxDiff = 0
for i in range(1, n-1) :
  diff = (abs(axis[i+1][0]-axis[i][0])+abs(axis[i+1][1]-axis[i][1])+abs(axis[i][0]-axis[i-1][0])+abs(axis[i][1]-axis[i-1][1]))-(abs(axis[i+1][0]-axis[i-1][0])+abs(axis[i+1][1]-axis[i-1][1]))
  maxDiff = max(diff, maxDiff)
  
xAxis = axis[0][0]
yAxis = axis[0][1]
totalValue = 0
for i in range(1, n) :
  totalValue += (abs(axis[i][0]-xAxis)+abs(axis[i][1]-yAxis))
  xAxis = axis[i][0]
  yAxis = axis[i][1]
  
print(totalValue - maxDiff)