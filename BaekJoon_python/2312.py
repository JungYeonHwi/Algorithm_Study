t = int(input())

for i in range(t) :
    num = int(input())
    for i in range(2, num + 1) :
        count = 0
        
        if num % i == 0 :
            while num % i == 0 :
                num = num // i
                count += 1
                
            print('%d %d' %(i, count))
        elif num == 1 : break