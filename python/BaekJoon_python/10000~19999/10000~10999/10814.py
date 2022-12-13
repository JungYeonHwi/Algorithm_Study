n = int(input())
List = []

for _ in range(n) : 
    a, b = map(str, input().split())
    List.append([int(a), b])
    
List = sorted(List, key=lambda a: a[0]) 

for i in List :
    print(i[0], i[1])