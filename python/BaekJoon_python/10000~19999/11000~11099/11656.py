s = input()
List = []

for _ in s : 
    List.append(s)
    s = s[1:]
    
for i in sorted(List) : 
    print(i)