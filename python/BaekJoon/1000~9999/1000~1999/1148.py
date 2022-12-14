import sys
from collections import defaultdict

input = sys.stdin.readline

arr = []

def check(keyword, dictionary) :
    keywordIdx = 0
    dictionaryIdx = 0
    
    while keywordIdx < len(keyword) and dictionaryIdx < len(dictionary) :
        if keyword[keywordIdx] == dictionary[dictionaryIdx] :
            keywordIdx += 1
            dictionaryIdx += 1
            if keywordIdx == len(keyword) : return True
        else : 
            dictionaryIdx += 1
            if dictionaryIdx == len(dictionary) : return False
    return False


while 1 :
    tmp = input().rstrip()
    if tmp == '-' : break
    else : arr.append(sorted(list(tmp)))

while 1 :
    tmp = input().rstrip()
    board = sorted(list(tmp))
    if tmp == '#': break
    else :
        cnt = defaultdict(int)
        for word in arr : 
            if check(word, board) :
                for w in set(word) :
                    cnt[w] += 1
    for i in set(tmp) :
        if i not in cnt : cnt[i] = 0

    most = max(cnt.values())
    least = min(cnt.values())
    mostArr = []
    leastArr = []
    for key, val in cnt.items():
        if val == most : mostArr.append(key)
        if val == least : leastArr.append(key)

    print(''.join(sorted(leastArr)), end=' ')
    print(least, end=' ')
    print(''.join(sorted(mostArr)), end=' ')
    print(most)