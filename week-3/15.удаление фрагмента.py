s = input()
pos1 = s.find("h")
pos2 = len(s) - s[::-1].find("h") - 1
print(s[0:pos1] + s[pos2 + 1:])
