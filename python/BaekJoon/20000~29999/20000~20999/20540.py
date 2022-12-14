s = input()
arr = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
for c in s : arr.remove(c)

answer = ''.join(arr)
print(answer)