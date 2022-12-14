NList = []

for i in range(9) : 
    NList.append(int(input()))

maxValue = max(NList)

print(maxValue)
print(NList.index(maxValue)+1)