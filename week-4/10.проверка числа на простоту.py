def IsPrime(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        elif i > n ** 0.5:
            return n
        i += 1


n = int(input())
if n == IsPrime(n):
    print("YES")
else:
    print("NO")
