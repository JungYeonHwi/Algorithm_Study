s = input()
List = []

for _ in s : 
    List.append(s)
    s = s[1:]
    
arr = sorted(List)

for i in arr : 
    print(List.index(i))