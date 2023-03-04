arr = [input() for _ in range(int(input()))]
arr.sort(key=lambda x:float(x))
print(arr[1])