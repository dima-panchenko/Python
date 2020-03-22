def powN():
    n = int(input())
    b = n**0.5
    x = b * 10 % 10
    z = x / 10
    global i
    if n != 0:
        if z == 0:
            powN()
            i += 1
            print(n, " ", end="")
        if z != 0:
            powN()


i = 0
powN()
if i == 0:
    print(0)
