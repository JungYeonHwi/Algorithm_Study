import sys
from collections import Counter

N = int(sys.stdin.readline())
List = []

for i in range(N) : 
    List.append(int(sys.stdin.readline()))
    
print(round(sum(List)/N))

List.sort()
print(List[N//2])

mostList = Counter(List).most_common()
if len(mostList) > 1 and mostList[0][1] == mostList[1][1] :
    print(mostList[1][0])
else :
    print(mostList[0][0])
    
print(max(List) - min(List))