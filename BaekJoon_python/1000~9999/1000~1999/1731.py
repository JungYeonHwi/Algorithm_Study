N = int(input())
List = []

for _ in range(N) : 
    n = int(input())
    List.append(n)
    
if (List[1] - List[0] == List[2] - List[1]) : 
    num = List[N-1]
    m = List[1] - List[0]
    print(num + m)
else : 
    num = List[N-1]
    m = List[1] // List[0]
    print(num * m)