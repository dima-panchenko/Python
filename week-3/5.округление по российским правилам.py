from math import floor, ceil
n = float(input())
fp = (n * 10 % 10) / 10
if fp >= 0.5:
    print(ceil(n))
else:
    print(floor(n))
