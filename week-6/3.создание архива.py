listInput = list(map(int, input().split()))
i = 0
listNum = []
while i < listInput[1]:
    n = int(input())
    listNum.append(n)
    i += 1
listNum.sort()
k = 0
size = listInput[0]
col = 0
while k < listInput[1]:
    if size - listNum[k] >= 0:
        size -= listNum[k]
        col += 1
        k += 1
    else:
        break
print(col)
