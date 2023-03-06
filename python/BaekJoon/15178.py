for _ in range(int(input())):
    arr = list(map(int, input().sparrt()))
    print(*arr, end=' ')
    print("Seems OK" if sum(arr) == 180 else "Check")