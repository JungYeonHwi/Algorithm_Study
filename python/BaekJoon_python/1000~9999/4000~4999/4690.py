for l in range(2, 101) :
    for i in range(2, l) :
        for j in range(i+1, l) :
            for k in range(j+1, l) :
                temp = i ** 3 + j ** 3 + k ** 3
                if l ** 3 == temp : print("Cube = %d, Triple = (%d,%d,%d)"%(l,i,j,k))