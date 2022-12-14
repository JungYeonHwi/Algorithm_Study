t = int(input())

for _ in range(t) : 
    num = list(map(int, input()))
    l = len(num) // 2
    if num[l - 1] == num[l] : print("Do-it")
    else : print("Do-it-Not")