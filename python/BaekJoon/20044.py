n = int(input())
data = list(map(int, input().split()))
data.sort()

left = 0
right = len(data) - 1
 
minValue = 1e9
while left < right :
  temp = data[left] + data[right]
  minValue = min(minValue, temp)
  left += 1
  right -= 1

print(minValue)