for _ in range(3):
    total = 0 # 선생님한테 받은 전체 금액
    coins = [] 
   
    # input 받으면서 전체 액수 구하기
    for _ in range(int(input())):
        C, N = map(int, input().split())
        total += C * N
        coins.append([C, N])

    # 홀수는 반으로 안나눠짐 > 굳이 확인 안해봐도 됨
    if total % 2 == 1:
        print(0)
        continue

    total //= 2
    # dp[n]의 의미 == 주어진 동전들로 n원을 만들 수 있는가?
    dp = [True] + [False] * total

    answer = 0
    for i in range(len(coins)):
        C, N = coins[i]
        
        # 거꾸로 탐색하면서 지불 가능한 액수 갱신
        for n in range(total, C-1, -1):
            if dp[n-C]:
                for j in range(N):
                    if n + C * j <= total:
                        dp[n + C * j] = True
                    else:
                        break
                        
        if dp[-1]: # 반띵 가능!
            answer = 1
            break

    print(answer)
