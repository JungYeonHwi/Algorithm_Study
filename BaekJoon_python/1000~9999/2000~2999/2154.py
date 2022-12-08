value = ""
for i in range(1, 100001):
    value += str(i)

print(value.index(input()) + 1)