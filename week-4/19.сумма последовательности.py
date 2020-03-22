def rec():
    n = int(input())
    global sumN
    if n != 0:
        sumN += n
        rec()
        return sumN
    if n == 0:
        return 0


sumN = 0
print(rec())
