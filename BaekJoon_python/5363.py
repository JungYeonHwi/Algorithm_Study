count = int(input())
words = []
 
for i in range(count) :
    word = input().split()
    words.append(word)
 
for i in range(count) :
    print(" ".join(words[i][2:len(words[i])]) +" "+ " ".join(words[i][0:2]))