N = int(input())
if N == 0 : print("divide by zero")
else : 
    arr = list(map(int, input().split()))
    ans = sum(arr)/N / (sum(arr)/N)
    print("%.2f" % ans)