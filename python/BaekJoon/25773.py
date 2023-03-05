number = input()

nl = list(number)

maxValue = sorted(nl, reverse=True)

answer = "".join(maxValue)
print(answer)