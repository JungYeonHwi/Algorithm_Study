while 1 :
    try:
        s = input()
        print(bytearray.fromhex(s).decode())

    except EOFError:
        break