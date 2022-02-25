N = int(input())
List0 = []
List1 = []

for i in range(N) : 
    num = input()
    
    if num == '1' : List1.append(i)
    else : List0.append(i)
    
if (len(List1) > len(List0)) : print("Junhee is cute!")
elif (len(List1) < len(List0)) : print("Junhee is not cute!")