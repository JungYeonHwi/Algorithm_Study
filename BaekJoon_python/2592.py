from collections import Counter

List = []
for i in range(10) :
    List.append(int(input()))
    
print(int(sum(List)/10))

item = Counter(List)
print(item.most_common(1)[0][0])