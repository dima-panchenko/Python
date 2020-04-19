n = int(input())
listNum = set(list(map(int, input().split())))
answer = input()
listNum2 = input()
if answer == "NO":
    listNum = set(range(1, n + 1)) - listNum
while listNum2 != 'HELP':
    answer2 = input()
    listNum3 = input()
    if answer2 == "YES":
        listNum &= set(list(map(int, listNum2.split())))
    else:
        listNum -= set(list(map(int, listNum2.split())))
    listNum2 = listNum3
print(*sorted(listNum))
