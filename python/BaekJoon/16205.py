import sys
import re
from unittest import result

t, name = sys.stdin.readline().strip().split()

firstWord = [name[0]]
rootWords = []  

if t == '1' :
    rootWords = re.findall('[A-Z][a-z]*', name)

    for i in range(1,len(name)):
        if name[i].isupper():
            break
        else:
            firstWord[-1] += name[i]
    rootWords = firstWord + rootWords

elif t == '2' :
    rootWords = name.split('_')

elif t == '3' :
    rootWords = re.findall('[A-Z][a-z]*', name)

for i in range(len(rootWords)) :
    rootWords[i] = rootWords[i].title()
result3 = "".join(rootWords)

rootWords[0] = rootWords[0].lower()
result1 = "".join(rootWords)

for i in range(1, len(rootWords)) :
    rootWords[i] = rootWords[i].lower()
result2 = "_".join(rootWords)

print(result1)
print(result2)
print(result3)
