N, C = map(int, input().split())
arr = []
vhrwnr = ["0" for i in range(C + 1)]

for _ in range(N) : 
    num = int(input())
    if num == 1 :
        print(C)
        quit()
    for k in range(num, C+1, num) :
        vhrwnr[k] = "1"

print(vhrwnr.count("1"))