List = []

for i in range(10) : 
    n = int(input())
    List.append(n%42)
    
setList = set(List)
print(len(setList))