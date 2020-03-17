n = int(input())
sumX = 0
sumS = 0
i = 0
while n != 0:
    sumX += n**2
    sumS += n
    i += 1
    n = int(input())
s = sumS / i
totalSum = sumX - 2 * s * sumS + i * (s**2)
print((totalSum / (i - 1))**0.5)
