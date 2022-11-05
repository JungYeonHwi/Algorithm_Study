arr = list(map(int, input().split()))
s = sum(arr)

if s > 370 : print("hacker")
elif s < 100 : print("none")
else : print("draw")