listNum = list(map(int, input().split()))
grades = [0] * 101
for now in listNum:
    grades[now] += 1
for grade in range(len(grades)):
    for i in range(grades[grade]):
        print(grade, end=" ")
