n = int(input())
List = []

for _ in range(n) : 
    weight, height = map(int, input().split())
    List.append((weight, height))

for i in List:
    rank = 1
    
    for j in List:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")