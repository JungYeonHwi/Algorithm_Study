t = int(input())

for i in range(t) : 
    n = input()
    
    if "D" in n : print(len(n[:n.index("D")]))
    else : print(len(n))