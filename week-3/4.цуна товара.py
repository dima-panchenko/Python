import math
prise = float(input())
rub = int(prise)
cop = math.ceil((prise * 100) % 100)
print(rub, cop)
