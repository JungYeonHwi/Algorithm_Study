h, w = map(int, input().split())
a, b = max(h, w), min(h, w)

arr1 = a/3 if a/3 <= b else b
arr2 = b/2
print(max(arr1, arr2))