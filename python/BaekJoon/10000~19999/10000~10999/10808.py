word = input()
result = [0] * 26
 
for i in word:
    result[ord(i) - 97] = word.count(i)
    
for i in result :
    print(i, end=" ")