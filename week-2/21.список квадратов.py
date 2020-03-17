n = int(input())
x = 0
i = 1
while x < n:
    x = i**2
    if x > n:
        break
    print(x, end=" ")
    i += 1
