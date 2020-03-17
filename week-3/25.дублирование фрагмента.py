s = input()
pos1 = s.find("h")
pos2 = s.rfind("h")
newS = s[pos1 + 1:pos2]
print(s[:pos1 + 1] + newS + newS + s[pos2:], sep="")
