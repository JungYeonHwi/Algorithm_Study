List = []

for i in range(9) : 
    n = int(input())
    List.append(n)

for i in range(0, 9) : 
    for j in range(i+1, 9) : 
       if sum(List) - (List[i] + List[j]) == 100:
            temp1 = List[i]
            temp2 = List[j]
 
List.remove(temp1)
List.remove(temp2)

List.sort()

for k in List : 
    print(k)