matrix = [input() for _ in range(5)]
N = (len(matrix[0])//4)+1

zero = ['***','* *','* *','* *','***']
one = ['  *','  *','  *','  *','  *']
two = ['***','  *','***','*  ','***']
three = ['***','  *','***','  *','***']
four  = ['* *','* *','***','  *','  *']
five = ['***','*  ','***','  *','***']
six = ['***','*  ','***','* *','***']
seven = ['***','  *','  *','  *','  *']
eight = ['***','* *','***','* *','***']
nine = ['***','* *','***','  *','***']
nums = [zero, one, two, three, four, five, six, seven, eight, nine]

check = [False] * 5
ca = [False] * 10
arr = []

for i in range(N) :
    for n in range(10) :
        for j in range(5) :
            if matrix[j][i*4 : i*4+3] == nums[n][j] :
                check[j] = True
        if all(check) :
            ca[n] = True
            arr.append(n)
        check = [False] * 5
    if any(ca) :
        ca = [False] * 10
        continue
    else :
        print("BOOM!!")
        exit()
        
ans = 0
for i in range(1, N+1):
    ans += arr[-i] * (10 ** (i-1))

if ans % 6 == 0 : print("BEER!!")
else : print("BOOM!!")