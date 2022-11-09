geminis = list(map(int, input().strip().split()))
startlink = list(map(int, input().strip().split()))
gSum, sSum, flag = 0, 0, False

for i in range(9):
    gSum+=geminis[i]
    if gSum > sSum:flag=True
    sSum += startlink[i]
    
if gSum < sSum and flag : print("Yes")
else : print("No")