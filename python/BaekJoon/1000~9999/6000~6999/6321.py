num = 0

for _ in range(int(input())) : 
    s = input()
    num += 1
    answer = ''
    for i in s :
        if i == "Z" : answer += "A"
        else : answer += chr(ord(i)+1)
    
    print("String #" + str(num))
    print(answer)
    print()