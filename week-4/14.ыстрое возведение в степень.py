def power(a, b):
    if b != 0:
        if b % 2 != 0:
            return a * power(a, b - 1)
        elif b % 2 == 0:
            return power(a**2, b / 2)
    else:
        return 1


a = float(input())
n = int(input())
print(power(a, n))
