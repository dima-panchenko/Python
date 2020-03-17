s = input()
pos1 = s.find("f")
pos2 = len(s) - s[::-1].find("f") - 1
if pos1 != -1:
    if pos1 != pos2:
        print(pos1, pos2)
    elif pos1 == pos2:
        print(pos1)
