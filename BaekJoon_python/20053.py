for _ in range(int(input())):
    N = int(input())
    arr = sorted(map(int, input().split()))
    print(arr[0], arr[-1])