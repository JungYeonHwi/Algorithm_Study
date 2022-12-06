N = list(map(int, str(input())))
dict = {2:0, 0:0, 1:0, 8:0} 
answer = False

for i in N :
    try :
        dict[i] += 1
    except : 
        print(0)
        answer = True
        break
        
if answer == False :
    if dict[2] != 0 and dict[0] != 0 and dict[1] != 0 and dict[8] != 0 :
        if dict[2] == dict[0] == dict[1] == dict[8] :
            print(8)
        else :
            print(2)
    else :
        print(1)