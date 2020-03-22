a = float(input())
n = int(input())
k = 1
if n > 0:
    while n != 0:
        k *= a
        n -= 1
    print(k)
elif n < 0:
    while n != 0:
        k *= a
        n += 1
    print(1/k)
else:
    print(1)
