T = int(input())

for i in range(T) :
    answer = 0
    S = input()

    while S != "6174" :
        bigger = int(''.join(sorted(S, reverse=True)))
        smaller = int(''.join(sorted(S)))
        S = str(bigger - smaller)

        if len(S) < 4 :
            temp = ""
            for i in range(4 - len(S)) :
                temp += '0'
            S = temp + S

        answer += 1

    print(answer)