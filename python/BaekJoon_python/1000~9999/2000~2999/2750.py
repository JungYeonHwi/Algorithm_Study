N = int(input())

List = []

for i in range(N) : 
    List.append(int(input()))
    
List.sort()

for i in List : 
    print(i)