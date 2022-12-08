n = int(input())
first = n
while n!=0 :
    if n > 1 :
        if n-1 > 1 :
            print("%d bottles of beer on the wall, %d bottles of beer."%(n,n))
            print("Take one down and pass it around, %d bottles of beer on the wall."%(n-1))
        else :
            print("%d bottles of beer on the wall, %d bottles of beer." % (n, n))
            print("Take one down and pass it around, 1 bottle of beer on the wall.")
    elif n == 1 :
        print("%d bottle of beer on the wall, %d bottle of beer." % (n, n))
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    print()
    n -= 1
if n == 0 :
    if first != 1 :
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, %d bottles of beer on the wall."%first)
    else :
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, %d bottle of beer on the wall." % first)