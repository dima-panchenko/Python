numList = list(map(int, input().split()))
i = 0
k = 0
num = 0
while i < len(numList):
    if numList[i] >= k:
        k = numList[i]
        num = i
    i += 1
print(k, num)
