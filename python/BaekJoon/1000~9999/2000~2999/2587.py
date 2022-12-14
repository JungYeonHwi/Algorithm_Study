List = []

for i in range(5) : 
    n = int(input())
    List.append(n)

print(int(sum(List) / 5))
List.sort()
print(List[2])