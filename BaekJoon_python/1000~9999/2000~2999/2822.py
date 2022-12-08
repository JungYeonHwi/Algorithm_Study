List = []

for i in range(8) : 
    num = int(input())
    List.append(num)
    
sortedList = sorted(List, reverse=True)

big = []
idx = []

for i in range(5) : 
    big.append(sortedList[i])
    
s = sum(big)

for k in big : 
    idx.append(List.index(k)+1)
    
sortedIdx = sorted(idx)
    
print(s) 

for i in sortedIdx : 
    print(i, end=' ')