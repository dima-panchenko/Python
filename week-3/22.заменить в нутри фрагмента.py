s = input()
pos1 = s.find("h")
pos2 = s.rfind("h")
newS = s[pos1 + 1:pos2]
if len(newS) != 0:
    print(s[:pos1 + 1], newS.replace("h", "H"), s[pos2:], sep="")
else:
    print(s)
