def rec():
    n = int(input())
    if n != 0:
        rec()
        print(n)
    if n == 0:
        print(0)


rec()
