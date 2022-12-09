import string
uppers = list(string.ascii_uppercase)
numbers = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
stroke = dict(zip(uppers, numbers))

me = input()
her = input()

meArr = list(me)
herArr = list(her)

name = []
score = []

length = len(me+her)

for i in range(length) :
    if i % 2 == 0 : name.append(meArr.pop(0))
    else : name.append(herArr.pop(0))

for i in name : score.append(stroke[i])


while length != 2 :
    now = []
    for i in range(length-1) : 
        now.append((score[i] + score[i + 1]) % 10)
    length -= 1
    score = now 
now = map(str, now)
print("".join(now))