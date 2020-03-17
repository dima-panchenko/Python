s = input()
pos1 = s.find("f")
pos2 = s.find("f", pos1 + 1)
if pos1 != -1:
    if pos2 != -1:
        print(pos2)
    else:
        print(-1)
else:
    print(-2)
