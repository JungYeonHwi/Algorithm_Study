n = int(input())
List = []

for _ in range(n) : 
    List.append(input())
    
for i in List : 
    if i[::-1] in List : 
        length = len(i)
        center = i[length // 2]
        break
    
print(length, center)