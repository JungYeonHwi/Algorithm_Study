n = int(input())
six = 666
count = 0

while 1:
    if '666' in str(six) : 
        count += 1
        print(str(six))            
    if count == n :          
        print(six)          
        break               
    six += 1    