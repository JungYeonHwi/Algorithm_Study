def prime(num) : 
    answer = 0
    for i in range(1, num) :
        if num % i == 0 : 
            answer += i

    return answer

for _ in range(int(input())) : 
    n = int(input())
    if prime(n) == n : print(n, "is a perfect number.\n")
    elif prime(n) < n : print(n, "is a deficient number.\n")
    elif prime(n) > n : print(n, "is an abundant number.\n")