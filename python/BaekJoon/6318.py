i = 1
while 1:
    n = int(input())
    if n == 0:
        break
    li = list(map(int, input().split()))
    cnt = 0
    while li != [li[0]]*n:
        max_i = li.index(max(li))
        li[max_i] -= 1
        min_i = li.index(min(li))
        li[min_i] += 1
        cnt += 1
    print(f"Set #{i}")
    print(f"The minimum number of moves is {cnt}.")
    print()
    i += 1