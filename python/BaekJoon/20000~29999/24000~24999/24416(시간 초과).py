def fib(n) :
    global cnt1
    cnt1 += 1
    if n == 1 or n == 2 :
        cnt1 -= 1
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

dp = {1 : 1, 2 : 1}
def fib2(n) :
    global cnt2

    if n in dp :
        return dp[n]

    else :
        dp[n] = fib2(n - 1) + fib2(n  - 2)
        cnt2 += 1
        return dp[n]
    
n = int(input())
cnt1, cnt2 = 0, 0
fib(n)
fib2(n)
print(cnt1 + 1, cnt2)