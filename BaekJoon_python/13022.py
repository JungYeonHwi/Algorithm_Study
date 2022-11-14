def check(word, start, end):
    length = (end - start + 1) // 4
    nw = 'w' * length + 'o' * length + 'l' * length + 'f' * length
    if word[start:end+1] == nw:
        return True
    return False

word = input()
idx = []
for i in range(len(word)):
    if word[i] == 'f' and (i == len(word) - 1 or word[i + 1] != 'f'):
        idx.append(i)
        
idx.append(len(word) - 1)
prev = 0

for idx, ind in enumerate(idx) :
    if (ind + 1) % 4 :
        print(0)
        break
    if not check(word, prev, ind) :
        print(0)
        break
    prev = ind + 1
print(1)