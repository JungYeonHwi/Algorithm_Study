tmp = (list(map(int, input().split())))
ans = tmp.index(int(input())) + 1
if ans < 6 : print("A+")
elif ans < 16 : print("A0")
elif ans < 31 : print("B+")
elif ans < 36 : print("B0")
elif ans < 46 : print("C+")
elif ans < 49 : print("C0")
else : print("F")