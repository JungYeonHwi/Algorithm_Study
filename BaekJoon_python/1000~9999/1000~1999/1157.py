words = input().upper()
unique = list(set(words))

List = []
for x in unique :
    cnt = words.count(x)
    List.append(cnt)

if List.count(max(List)) > 1 :
    print('?')
else :
    max_index = List.index(max(List))
    print(unique[max_index])