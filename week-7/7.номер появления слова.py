inInput = open("input.txt")
myList = inInput.readlines()
words = []
col = 0
for i in range(len(myList)):
    lines = myList[i].split()
    words += lines
mySet = set()
myDict = {}
col = 0
for i in words:
    if i in mySet:
        if i not in myDict:
            myDict[i] = []
        myDict[i] += 1
        print(myDict[i], end=" ")
    else:
        if i not in myDict:
            myDict[i] = []
        myDict[i] = 0
        print(myDict[i], end=" ")
    mySet.add(i)
