for _ in range(int(input())):
    N = int(input())
    arr1 = set(map(int, input().split()))
    M = int(input())
    arr2 = list(map(int, input().split()))
    for n in arr2 :
        print(1 if n in arr1 else 0)