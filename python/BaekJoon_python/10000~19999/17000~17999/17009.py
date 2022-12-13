arr1 = [int(input()) for _ in range(3)]
arr2 = [int(input()) for _ in range(3)]
A = arr1[0] * 3 + arr1[1] * 2 + arr1[2]
B = arr2[0] * 3 + arr2[1] * 2 + arr2[2]

if A == B : print("T")
elif A > B : print("A")
else : print("B")