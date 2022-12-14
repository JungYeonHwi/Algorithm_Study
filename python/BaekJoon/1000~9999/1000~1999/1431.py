n = int(input())

def s(inputs):
    result = 0
    for i in inputs :
        if i.isdigit() : result += int(i)
    return result

arr = []
for i in range(n) :
    arr.append(input())

arr.sort(key = lambda x :(len(x), s(x), x))

for i in arr :
    print(i)