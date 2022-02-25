V = int(input())
List = list(map(str, input()))
AList = []
BList = []

for i in List : 
    if i == 'A' : AList.append(i)
    else : BList.append(i)
    
if (len(AList) > len(BList)) : print("A")
elif (len(AList) < len(BList)) : print("B")
else : print("Tie")