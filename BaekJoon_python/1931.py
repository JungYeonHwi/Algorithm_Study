n = int(input())
List = []

for _ in range(n) : 
    a, b = map(int, input().split())
    List.append([a, b])
    
List = sorted(List, key=lambda a: a[0])
List = sorted(List, key=lambda a: a[1]) 

last = 0 
conut = 0

for i, j in List :
  if i >= last :
    conut += 1
    last = j

print(conut)