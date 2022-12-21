n = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()
print(arr[(n-1)//2])