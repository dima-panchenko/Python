k = int(input())
x = float(input())
p = k
i = 0
sumP = 0
while i < k:
    n = float(input())
    sumP += n * (x**p)
    p -= 1
    i += 1
n0 = float(input())
print(sumP + n0)
