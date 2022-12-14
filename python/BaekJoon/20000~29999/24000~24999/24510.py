c=int(input())

maxValue=0

for _ in range(c):
    Str=input()
    Count=0

    Count+=Str.count("for")
    Count+=Str.count("while")

    if Count > maxValue :
        maxValue=Count

print(maxValue)