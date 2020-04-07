numList = list(map(int, input().split()))
i = 0
k = 0
maxN = 0
num1 = 0
num2 = 0
while i < len(numList):
    if numList[i] > maxN:
        maxN = numList[i]
        num1 = i
    i += 1
minN = maxN
while k < len(numList):
    if numList[k] < minN:
        minN = numList[k]
        num2 = k
    k += 1
numList[num1], numList[num2] = numList[num2], numList[num1]
print(*numList)
