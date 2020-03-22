def ReduceFraction(n, m):
    if n % 2 == 0 and m % 2 == 0:
        while n % 2 == 0 and m % 2 == 0:
            n /= 2
            m /= 2
    if n % 3 == 0 and m % 3 == 0:
        while n % 3 == 0 and m % 3 == 0:
            n /= 3
            m /= 3
    if n % 5 == 0 and m % 5 == 0:
        while n % 5 == 0 and m % 5 == 0:
            n /= 5
            m /= 5
    if n % 7 == 0 and m % 7 == 0:
        while n % 7 == 0 and m % 7 == 0:
            n /= 7
            m /= 7
    if n % m == 0:
        while n % m == 0 and m != 1:
            n /= m
    if m % n == 0:
        while m % n == 0 and n != 1:
            m /= n
    return int(n), int(m)


a = int(input())
b = int(input())
print(*ReduceFraction(a, b))
