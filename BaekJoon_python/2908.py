A, B = input().split()

AList = list(A)
BList = list(B)

AList.reverse()
BList.reverse()

AReverse = "".join(AList)
BReverse = "".join(BList)

if (AReverse > BReverse) : print(AReverse)
else : print(BReverse)