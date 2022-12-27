arr = list(map(int, input()))

if len(arr) <= 2 : print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else : 
    d = arr[0] - arr[1]
    check = 1
    
    for i in range(1, len(arr) - 1) : 
        value = arr[i] - arr[i+1]
        
        if d != value : 
            check = 0
            break

    if check : print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    else : print("흥칫뿡!! <(￣ ﹌ ￣)>")