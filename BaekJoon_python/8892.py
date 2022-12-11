def palindrome():
    n = int(input())
    arr = [input() for _ in range(n)]

    l = len(arr)
    for i in range(l) :
        for j in range(l) :
            if i != j:
                word = arr[i] + arr[j]
                if word == word[::-1] : return word

    return 0


t = int(input())
while t > 0 :
    answer = palindrome()
    print(0) if answer == 0 else print(answer)
    t -= 1