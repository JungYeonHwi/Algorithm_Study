arr = list(map(int, input().split()))
copy = list(arr)
copy.sort()

if copy == arr : print("Good")
else : print("Bad")